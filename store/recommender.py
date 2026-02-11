import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from .models import Product
from typing import Optional, List, Dict, Any

# Try to import the Cython-optimized similarity function
try:
    from .cython_utils.fast_similarity import cosine  # type: ignore
    CYTHON_AVAILABLE = True
except ImportError:
    CYTHON_AVAILABLE = False
    cosine = None  # type: ignore


class SimpleRecommender:
    def __init__(self) -> None:
        self._fitted = False
        self.ids: List[int] = []
        self.vectorizer: Optional[TfidfVectorizer] = None
        self.tfidf: Any = None
        self.sim: Optional[np.ndarray] = None

    def fit(self) -> None:
        """Fit the recommendation model using product descriptions."""
        products = list(Product.objects.all())
        self.ids = [p.pk for p in products]
        corpus = [p.description or p.name for p in products]
        if not corpus:
            self.tfidf = None
            self.sim = None
            self._fitted = True
            return
        
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf = self.vectorizer.fit_transform(corpus)
        
        # Use optimized similarity calculation if Cython is available
        if CYTHON_AVAILABLE and self.tfidf.shape[0] > 0:
            try:
                # Convert to dense array and compute similarity using Cython
                tfidf_dense = self.tfidf.toarray().astype(np.float64)  # type: ignore
                n = len(tfidf_dense)
                self.sim = np.zeros((n, n), dtype=np.float64)
                
                # Use Cython-optimized cosine similarity for each pair
                for i in range(n):
                    for j in range(n):
                        self.sim[i, j] = cosine(tfidf_dense[i], tfidf_dense[j])  # type: ignore
            except Exception:
                # Fallback to sklearn if Cython fails
                self.sim = linear_kernel(self.tfidf, self.tfidf)
        else:
            # Use sklearn's fast kernel method
            try:
                self.sim = linear_kernel(self.tfidf, self.tfidf)
            except Exception:
                self.sim = (self.tfidf * self.tfidf.T).toarray()  # type: ignore
        
        self._fitted = True

    def recommend_by_product(self, product_id: int, topn: int = 5, session: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Recommend products similar to a given product."""
        if not self._fitted:
            self.fit()
        if self.tfidf is None:
            return []
        try:
            idx = self.ids.index(product_id)
        except ValueError:
            return []
        
        if self.sim is None:
            return []
        
        sims = list(enumerate(self.sim[idx]))
        sims = sorted(sims, key=lambda x: x[1], reverse=True)
        recs = []
        for i, score in sims[1: topn + 1]:
            recs.append({'id': self.ids[i], 'score': float(score)})
        return recs

    def recommend_for_session(self, session: Dict[str, Any], topn: int = 10) -> List[Dict[str, Any]]:
        """Generate recommendations based on user's liked products."""
        if not self._fitted:
            self.fit()
        likes = session.get('likes', [])
        if not likes:
            # Fallback: return first N products if no likes
            return [{'id': pid, 'score': 0.0} for pid in self.ids[:topn]]
        
        # Aggregate recommendations from all liked products
        agg: Dict[int, float] = {}
        for pid in likes:
            try:
                pid_int = int(pid)
            except Exception:
                continue
            recs = self.recommend_by_product(pid_int, topn=topn * 2, session=session)
            for r in recs:
                agg[r['id']] = agg.get(r['id'], 0.0) + r['score']
        
        items = sorted(agg.items(), key=lambda x: x[1], reverse=True)
        return [{'id': k, 'score': float(v)} for k, v in items[:topn]]


# Global recommender instance
_RECOMMENDER = SimpleRecommender()


def recommend_for_product(product_id: int, topn: int = 5, session: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """Public function to get recommendations for a specific product."""
    return _RECOMMENDER.recommend_by_product(product_id, topn=topn, session=session)


def recommend_for_session(session: Dict[str, Any], topn: int = 10) -> List[Dict[str, Any]]:
    """Public function to get session-based recommendations."""
    return _RECOMMENDER.recommend_for_session(session, topn=topn)


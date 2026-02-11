# Simple Django E-commerce with Recommendations
# E-Commerce with AI-Powered Recommendations

A Django-based e-commerce platform with machine learning product recommendations and Cython performance optimization.

## Features

- **Product Display & Management**: Browse and view products with descriptions and prices
- **Shopping Cart**: Add items to cart, view total, and proceed to checkout
- **ML-Based Recommendations**: Content-based recommendation engine using TF-IDF similarity on product descriptions
- **User Feedback System**: Like/dislike products to influence personalized recommendations
- **Cython Optimization**: Cosine similarity calculations optimized with Cython (fallback pure Python if not compiled)
- **Session-Based Persistence**: Cart and user preferences stored in Django sessions

## Installation & Setup

### Quick Start (Windows)

1. **Create and activate virtual environment**:
	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate.ps1
	```

2. **Install dependencies**:
	```powershell
	pip install -r requirements.txt
	```

3. **(Optional) Build Cython extension**:
	```powershell
	python setup.py build_ext --inplace
	```

4. **Run migrations and seed data**:
	```powershell
	python manage.py migrate
	python manage.py seed
	python manage.py runserver
	```

5. **Open browser**: http://127.0.0.1:8000/

## Features Tour

- **Browse Products**: Visit `/` to see all products
- **Product Details**: Click on a product to view details and AI-recommended similar items
- **Shopping Cart**: Add items, view total, checkout
- **Personalized Recommendations**: Like/dislike products → visit `/recommendations/` for personalized suggestions
- **Feedback System**: Provide feedback to improve recommendations

## Recommendation Engine

**Technology**: TF-IDF Content-Based Filtering

- Product descriptions are vectorized using TF-IDF
- Cosine similarity is computed between product vectors
- Recommendations based on products user has liked
- Cython-accelerated similarity calculations (optional; pure Python fallback included)

## Project Components

### Django Models
- `Product`: name, description, price, image_url

### Views & Templates
- `product_list`: Browse all products
- `product_detail`: View single product + recommendations
- `add_to_cart`: Session-based cart management
- `view_cart`: Cart summary & checkout
- `recommendations`: Personalized suggestions based on likes
- `feedback`: Like/dislike endpoint

### Recommendation System (`recommender.py`)
- `SimpleRecommender` class with TF-IDF vectorization
- `recommend_by_product()`: Get similar products
- `recommend_for_session()`: Personalized recommendations based on user likes

### Cython Optimization (`cython_utils/`)
- `fast_similarity.pyx`: Optimized cosine similarity (C extension)
- Graceful fallback to pure Python if not compiled

## Sample Data

5 products pre-seeded:
- Red T-Shirt ($19.99)
- Blue Jeans ($49.99)
- Sneakers ($79.99)
- Coffee Mug ($9.99)
- Wireless Mouse ($24.99)

## Submission

- **Deadline**: February 12, 2026
- **Technologies**: Django, Cython, scikit-learn, numpy
- **Tasks Completed**:
  ✓ Django e-commerce with product display, cart, checkout
  ✓ ML recommendation system (TF-IDF + cosine similarity)
  ✓ Cython optimization for similarity computation
  ✓ User interaction & feedback system
  ✓ Session-based persistence

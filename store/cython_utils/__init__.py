import numpy as np

def cosine(a, b):
    """Compute cosine similarity (fallback pure Python)."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    na = (a * a).sum() ** 0.5
    nb = (b * b).sum() ** 0.5
    if na == 0 or nb == 0:
        return 0.0
    return float((a @ b) / (na * nb))

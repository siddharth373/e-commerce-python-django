# cython: boundscheck=False
import cython
from libc.math cimport sqrt

@cython.boundscheck(False)
@cython.wraparound(False)
def cosine(double[:] a, double[:] b):
    cdef Py_ssize_t n = a.shape[0]
    cdef Py_ssize_t i
    cdef double dot = 0.0
    cdef double na = 0.0
    cdef double nb = 0.0
    for i in range(n):
        dot += a[i] * b[i]
        na += a[i] * a[i]
        nb += b[i] * b[i]
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot / (sqrt(na) * sqrt(nb))

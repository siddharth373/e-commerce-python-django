from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        'store.cython_utils.fast_similarity',
        ['store/cython_utils/fast_similarity.pyx'],
        include_dirs=[np.get_include()],
    )
]

setup(
    name='assignment_store_cython',
    ext_modules=cythonize(extensions, annotate=False),
)

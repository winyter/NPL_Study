from Cython.Build import cythonize
from distutils.core import setup, Extension

extensions = [
    Extension("integrate",
              ["integrate.pyx"],
              extra_compile_args = ["-O3"],
              extra_link_args=[]
              )
]
 
setup(
  name = "integrate",
  ext_modules = cythonize(extensions),
)
from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("wrap_integrate",
                sources=["wrap_integrate.pyx", "integrate.c"],
                extra_link_args=["-mmacosx-version-min=10.14"]
                )

setup(name="wrap_integrate", ext_modules=cythonize(ext))
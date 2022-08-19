from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('wtf_pokemon_openCV_v3.pyx', language_level = "3"))
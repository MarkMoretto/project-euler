"""
Purpose: Compile Cython scripts
Date created: 2019-12-21
URI: https://docs.python.org/3/distutils/apiref.html?highlight=build_ext
URI: https://github.com/Technologicat/setup-template-cython/blob/master/setup.py
"""

from setuptools import setup, Extension
from Cython.Distutils import build_ext
import numpy as np

NAME = "utilities"
VERSION = "0.1.1"
DESCR = "Small utility objects for processing data."
URL = ""
REQUIRES = ['cython']

AUTHOR = "Mark A. Moretto"
EMAIL = "otteromkram@gmail.com"

LICENSE = "MIT"

SRC_DIR = "utils"
PACKAGES = [SRC_DIR]

ext_1 = Extension(
    SRC_DIR + ".m_funcs",
    [SRC_DIR + "/m_funcs.pyx"],
    libraries=[],
    include_dirs=[np.get_include()],
)

ext_2 = Extension(
    SRC_DIR + ".m_math",
    [SRC_DIR + "/m_math.pyx"],
    libraries=[],
    include_dirs=[np.get_include()],
)

EXTENSIONS = [ext_1, ext_2]


if __name__ == "__main__":
    setup(
        install_requires=REQUIRES,
        packages=PACKAGES,
        zip_safe=False,
        name=NAME,
        version=VERSION,
        description=DESCR,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        cmdclass={"build_ext": build_ext},
        ext_modules=EXTENSIONS,
    )


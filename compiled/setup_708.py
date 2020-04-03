"""
Purpose: Compile Cython scripts
Date created: 2019-12-21
URI: https://docs.python.org/3/distutils/apiref.html?highlight=build_ext
URI: https://github.com/Technologicat/setup-template-cython/blob/master/setup.py
"""

# from setuptools import setup
# from Cython.Build import cythonize


# setup(
	# ext_modules=cythonize("utils\utils.pyx"),
# )

from setuptools import setup, Extension
from Cython.Distutils import build_ext
import numpy as np

NAME = "utilities708"
VERSION = "0.1.0"
DESCR = "Utility functions for project-euler problem 708."
URL = ""
REQUIRES = ['cython']

AUTHOR = "Mark A. Moretto"
EMAIL = "otteromkram@gmail.com"

LICENSE = "MIT"

SRC_DIR = "utils"
PACKAGES = [SRC_DIR]

ext_1 = Extension(
    SRC_DIR + ".utils",
    [SRC_DIR + "/utils708.pyx"],
    libraries=[],
    include_dirs=[np.get_include()],
)


EXTENSIONS = [ext_1,]


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


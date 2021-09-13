#!/usr/bin/env python
import setuptools
from distutils.core import setup
import re

long_description = """
A fork of the popular PyPDF2 library adding support to write
to compression-based file descriptors (ex. gzip.open). Codebase
is also being updated to support newer versions of Python 3.

A Pure-Python library built as a PDF toolkit.  It is capable of:

- extracting document information (title, author, ...)
- splitting documents page by page
- merging documents page by page
- cropping pages
- merging multiple pages into a single page
- encrypting and decrypting PDF files
- and more!

By being Pure-Python, it should run on any Python platform without any
dependencies on external libraries.  It can also work entirely on StringIO
objects rather than file streams, allowing for PDF manipulation in memory.
It is therefore a useful tool for websites that manage or manipulate PDFs.
"""

VERSIONFILE="Py3PDF/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE))

setup(
        name="Py3PDF",
        version=verstr,
        description="PyPDF2 fork",
        long_description=long_description,
        author="Jacod Shax",
        author_email="igotlocekdout2day@gmail.com",
        url="https://github.com/LateNightLearning/Py3PDF",
        classifiers = [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
        packages=["Py3PDF"],
    )

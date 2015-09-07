#!/usr/bin/env python
import os

from setuptools import setup, find_packages

HERE = os.path.dirname(__file__)

setup(
    name = "sandals",
    version = "0.2.0",
    description = "A fast gui inspired by Shoes",
    author = "Henry Schreiner",
    author_email = "henryiii@physics.utexas.edu",
    license = "MIT",
    url = "http://sandals.readthedocs.org",
    packages = find_packages(),
    platforms = ["POSIX", "Windows"],
    provides = ["sandals"],
    keywords = "gui, shoes, tkinter",
    long_description = open(os.path.join(HERE, "README.md"), "r").read(),
    classifiers = [
         "Development Status :: 5 - Production/Stable",
         "License :: OSI Approved :: MIT License",
         "Operating System :: Microsoft :: Windows",
         "Operating System :: POSIX",
         "Programming Language :: Python :: 2.6",
         "Programming Language :: Python :: 2.7",
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.3",
         "Programming Language :: Python :: 3.4",
         "Topic :: Software Development :: Build Tools",
         "Topic :: System :: Systems Administration",
    ],
)

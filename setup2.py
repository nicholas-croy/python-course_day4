# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:36:28 2022

@author: niccr151
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(name="fastloop", ext_modules=cythonize('fastloop.pyx'),)
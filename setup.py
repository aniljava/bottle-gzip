#!/usr/bin/env python

import sys
import os
from distutils.core import setup

setup(
    name = 'bottle_gzip',
    version = '0.1',
    description = 'Output compression for Bottle applications',
    author = 'Li Gang, Roy Shan',
    author_email = 'ligang at ibkon.com, roy at ibkon.com',
    license = 'MIT',
    platforms = 'any',
    py_modules = ['bottle_gzip'],
    requires = ['bottle (>=0.10)'],
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

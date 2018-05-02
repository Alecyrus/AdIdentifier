#!/usr/bin/env python  
from __future__ import print_function  
from setuptools import setup, find_packages  
import sys  
  
setup(  
    name="adidentifier",  
    version="0.0.8",  
    author="Alecyrus",  
    author_email="heyuangunia@gmail.com",  
    description="AdIdentifier",  
    long_description=open("README.md").read(),  
    license="MIT",  
    url="https://github.com/Alecyrus/AdIdentifier",  
    packages=['adidentifier'],
    package_dir={'adidentifier':'adidentifier'},
    package_data={'adidentifier':['*.*','model/*']},
    install_requires=[   
        "adblockparser",
        "tgrocery",
        "urlparse4",
        "python-Levenshtein",
        "jieba",
        "fuzzywuzzy"
        ],  
    classifiers=[  
        "Environment :: Web Environment",  
        "Intended Audience :: Developers",  
        "Operating System :: OS Independent",  
        "Topic :: Text Processing :: Indexing",  
        "Topic :: Utilities",  
        "Topic :: Internet",  
        "Topic :: Software Development :: Libraries :: Python Modules",  
        "Programming Language :: Python",  
        "Programming Language :: Python :: 2",  
        "Programming Language :: Python :: 2.7",  
    ], 
)  

#!/usr/bin/env python  
from __future__ import print_function  
from setuptools import setup, find_packages  
import sys  
  
setup(  
    name="adidentifier",  
    version="0.0.2",  
    author="Alecyrus",  
    author_email="heyuangunia@gmail.com",  
    description="AdIdentifier",  
    long_description=open("README.md").read(),  
    license="MIT",  
    url="https://github.com/Alecyrus/AdIdentifier",  
    packages=['adidentifier'],  
    install_requires=[  
        "re2",  
        "adblockparser",
        "tgrocery"
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

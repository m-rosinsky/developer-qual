"""
File:
    python/00_Introduction/setup.py

Brief:
    Package setup file. DO NOT MODIFY.
"""

from setuptools import setup, find_packages

setup(
    name='00_Introduction',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    test_suite='nose.collector',
    tests_require=['nose']
)

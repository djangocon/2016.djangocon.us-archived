#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='djangocon',
    version='1.0',
    description="",
    author="Mark Wirblich",
    author_email='mark@lincolnloop.com',
    url='',
    packages=find_packages(),
    package_data={'djangocon': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)

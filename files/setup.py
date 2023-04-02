#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='meow-v2',
    version=version,
    description='Ultimate phishing tool in python with dual tunneling, 77 templates and many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Keshavah-reddy',
    author_email='adhitechie@gmail.com',
    license="MIT",
    url='https://github.com/keshavah-reddy/meow-v2/',
    scripts=['meow-v2'],
    install_requires=["requests", "bs4", "rich"]
)

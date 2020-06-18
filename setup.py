# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mangosort',
    version='0.2.1',
    url='https://github.com/raulmangolin/mangosort',
    license='MIT License',
    author='Raul Mangolin',
    author_email='eu@raulmangolin.com',
    keywords='dictionary dict list sort keysort',
    description=u'Sort list by multiple keys and directions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['mangosort'],
    install_requires=[],
)

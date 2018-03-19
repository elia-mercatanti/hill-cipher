#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Hill Cipher',
    version='0.1.0',
    author='Elia Mercatanti',
    author_email='emercatanti@gmail.com',
    url='https://bitbucket.org/elia-mercatanti/hill-cipher',
    description='Implement the Hill cipher.',
    long_description=open('README.md').read(),
    license='LICENSE.txt',
    download_url='https://bitbucket.org/elia-mercatanti/hill-cipher',
    packages=['src'],
    platforms=['Windows', 'MacOS', 'UNIX', 'Linux']
)

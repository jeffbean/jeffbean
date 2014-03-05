# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='jeffbean',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/jeffbean/jeffbean',
    license='',
    setup_requires=['setuptools-git'],
    author='Jeffrey Bean',
    author_email='jrb3330@gmail.com',
    description="Jeff's Website",
    requires=['django>=1.6'],
    include_package_data=True,
)

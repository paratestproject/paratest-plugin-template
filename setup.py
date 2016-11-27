# -*- coding: utf-8 -*-
import os
import sys
import platform
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

def read_description():
    if not os.path.exists('README.rst'):
        return ""
    with open('README.rst') as fd:
        return fd.read()


setup(
    name='paratest-plugin-template',
    version='0.0.1',
    description="Test paralelizer template (does nothing)",
    long_description=read_description(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: '
        'Libraries :: Application Frameworks',
    ],
    keywords='parallel test plugin',
    author='Miguel Angel Garcia',
    author_email='miguelangel.garcia@gmail.com',
    url='https://github.com/paratestproject/paratest-plugin-template',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'paratest': 'find = paratest_plugin.plugin:find'
    }
)

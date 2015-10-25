#!/usr/bin/env python

from os.path import join, dirname

from setuptools import setup

import ymir


setup(
    name='ymir',
    version=ymir.__version__,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts': [
            'ymir = ymir:main',
            ],
        },
    install_requires=[
        "flask",
        "sqlalchemy",
        "flask-cors",
    ]
)

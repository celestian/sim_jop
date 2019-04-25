#!/usr/bin/env python3

from setuptools import setup

setup(
    name='sim_jop',
    version='0.0.1',
    packages=['sim_jop'],
    entry_points={
        'console_scripts': [
            'sim_jop = sim_jop.__main__:main'
        ]
    }
)

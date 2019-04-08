#!/usr/bin/env python3

from setuptools import setup

setup(
    name='sim_doz',
    version='0.0.1',
    packages=['sim_doz'],
    entry_points={
        'console_scripts': [
            'sim_doz = sim_doz.__main__:main'
        ]
    }
)

#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sjop-server",
    version="0.0.1",
    author="celestian",
    author_email="petr.celestian@gmail.com",
    description="sim_jop server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/celestian/sim_jop",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'sjop-server = sjop-server.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment :: Simulation",
        "Development Status :: 1 - Planning",
    ],
)

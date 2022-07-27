#!/usr/bin/env python3
import pathlib

from setuptools import setup

import zoomdl

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="zoom-downloader",
    version=zoomdl.__version__,
    description="Zoom recording downloader",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hykilpikonna/zoomdl",
    author="Olivier Cloux & Azalea Gui",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=['zoomdl'],
    package_data={'zoomdl': ['zoomdl/*']},
    include_package_data=True,
    install_requires=['setuptools', 'typing_extensions', 'requests~=2.28.1', 'demjson3~=3.0.5', 'tqdm~=4.64.0'],
    entry_points={
        "console_scripts": [
            "zoomdl=zoomdl:main",
        ]
    },
)

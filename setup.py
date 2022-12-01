"""Setup config."""

# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

LONG_DESC = "magicbag is a python tool library."

requires = []

setup(
    name="magicbag",
    url="https://github.com/lipicoder/magicbag",
    author="lipi",
    author_email="lipicoder@qq.com",
    description="python tools library",
    long_description=LONG_DESC,
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)

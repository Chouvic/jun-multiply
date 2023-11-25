from setuptools import setup

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="jun-multiply",
    version="0.0.2",
    description="Demo library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://jun-multiply.readthedocs.io/",
    author="Jun Zhou",
    author_email="example@email.com",
    license="MIT",
    packages=["jun_multiply"],
    include_package_data=True,
    install_requires=[
        "numpy",
    ]
)

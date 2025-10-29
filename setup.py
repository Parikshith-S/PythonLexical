from setuptools import setup, find_packages

setup(
    name="python-lexical",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pytest>=7.0.0',
        'pytest-cov>=4.0.0',
    ],
)

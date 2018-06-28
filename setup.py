import os
from setuptools import setup, find_packages

required = ['urllib','http.server','socketserver','requests','random']

setup(
    name = "WebConda",
    version = "0.0.4",
    author = "Isak Vukovic",
    author_email = "WebConda@gmail.com",
    description = ("Fast and Easy WebFramework"),
    packages=["WebConda"],       
    install_requires=required,
    license='MIT'
)
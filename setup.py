from setuptools import setup, find_packages

setup(
    name='openfactory',
    version='0.1.0',
    install_requires=[
        "repo @ https://github.com/rwuthric/PyKSQL.git",
        "repo @ https://github.com/rwuthric/python-mtc2kafka.git"
    ],
)

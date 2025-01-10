from setuptools import setup, find_packages

setup(
    name='openfactory',
    version='0.1.0',
    install_requires=[
        "PyKSQL @ https://github.com/rwuthric/PyKSQL.git",
        "python-mtc2kafka @ https://github.com/rwuthric/python-mtc2kafka.git"
    ],
)

#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = [
    'flask-restless',
    #'flask-restful',
    'iso8601',
    'psycopg2',
    'pytz',
    'SQLAlchemy',
    'simplejson',
    'voevent-parse>=0.9',
]

test_requires = [
    'pytest',
    'pytest-capturelog',
    'tox',
]

extras_require = {
    'test': test_requires,
    'all': test_requires,
}
packages = find_packages()
print
print "FOUND PACKAGES: ", packages

scripts = [
    "voeventdb/bin/voeventdb_create.py",
    "voeventdb/bin/voeventdb_ingest_tarball.py",
    "voeventdb/bin/voeventdb_dump_tarball.py",
]

setup(
    name="voeventdb",
    version="0.1a0",
    description="Data-store and accompanying RESTful query API for archiving "
                "and retrieving VOEvent packets.",
    author="Tim Staley",
    author_email="timstaley337@gmail.com",
    url="https://github.com/timstaley/voeventdb",
    packages=packages,
    package_data={'voeventdb':['tests/resources/*.xml']},
    install_requires=install_requires,
    extras_require=extras_require,
    scripts=scripts
)

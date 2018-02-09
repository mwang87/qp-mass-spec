#!/usr/bin/env python

# -----------------------------------------------------------------------------
# Copyright (c) 2018, Qiita development team.
#
# Distributed under the terms of the BSD 3-clause License License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------
from setuptools import setup
from glob import glob

__version__ = "0.1.0-dev"

classes = """
    Development Status :: 3 - Alpha
    License :: OSI Approved :: BSD License
    Topic :: Scientific/Engineering :: Bio-Informatics
    Topic :: Software Development :: Libraries :: Application Frameworks
    Topic :: Software Development :: Libraries :: Python Modules
    Programming Language :: Python
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: Implementation :: CPython
    Operating System :: POSIX :: Linux
    Operating System :: MacOS :: MacOS X
"""

with open('README.rst') as f:
    long_description = f.read()

classifiers = [s.strip() for s in classes.split('\n') if s]

setup(name='mass_spec Qiita Plugin',
      version=__version__,
      long_description=long_description,
      license="BSD",
      description='Qiita Type Plugin: mass_spec',
      author="Qiita development team",
      author_email="qiita.help@gmail.com",
      url='https://github.com/mass_spec/mass_spec',
      test_suite='nose.collector',
      packages=['mass_spec'],
      package_data={'mass_spec': ['support_files/config_file.cfg']},
      scripts=glob('scripts/*'),
      extras_require={'test': ["nose >= 0.10.1", "pep8"]},
      install_requires=['click >= 3.3', 'qiita_client'],
      classifiers=classifiers
      )

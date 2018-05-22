#!/usr/bin/env python
"""Becquerel: Tools for radiation spectral analysis.

TODO: longer description -- this portion will go into 'long_description'
in the setup metadata.

"""

from __future__ import print_function
from setuptools import setup


DOCLINES = (__doc__ or '').split('\n')

CLASSIFIERS = """\
Intended Audience :: Science/Research
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Topic :: Scientific/Engineering
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

MAJOR               = 0
MINOR               = 0
MICRO               = 0
VERSION             = '{}.{}.{}'.format(MAJOR, MINOR, MICRO)


# TODO: maintainer
# TODO: maintainer_email
# TODO: author
# TODO: license

setup(
    name = 'gauss_fit',
    description = DOCLINES[0],
    long_description = '\n'.join(DOCLINES[2:]),
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    platforms = ['Windows', 'Linux', 'Solaris', 'Mac OS-X', 'Unix'],
     packages=[
        'gauss_fit',
        #'becquerel.parsers',
        #'becquerel.tools',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    package_data={'gauss_fit': ['*.txt']}
)

#!/usr/bin/env python
'''
Setup script for the complot package
'''

__author__ = 'Marcos Romero Lamas'
__email__ = 'marromlam@gmail.com'
__license__ = 'MIT License Copyright (c) 2021 Marcos Romero Lamas'


# Modules {{{

import os
import sys
import setuptools
import subprocess
import textwrap

# }}}


# Version {{{
# Version of the package. Before a new release is made just the version_list
# must be changed. The options for the fourth tag are "dev", "alpha", "beta"
# and "final".
version_list = [1, 0, 0, 'dev', 0]

VERSION = f"{version_list[0]}.{version_list[1]}.{version_list[2]}"

tag = version_list[3]
if tag != 'final':
  if tag in ('alpha', 'beta', 'dev'):
    VERSION += f"{tag}{version_list[-1]}"
  else:
    raise ValueError(f'Unable to parse version tuple {version_list}')

# }}}


# Helpers {{{

def create_version_file():
    '''
    Create the file version.py given the version of the package.
    '''
    version_file = open('complot/version.py', 'wt')
    version_file.write(textwrap.dedent("""\
    '''
    Auto-generated module holding the version of the complot package
    '''

    VERSION = "{}"
    VERSION_INFO = {}

    __all__ = ['VERSION', 'VERSION_INFO']
    """.format(VERSION, version_list)))
    version_file.close()


def install_requirements():
  '''
  Read installation requirements from "requirements.txt" file.
  '''
  requirements = []
  with open('requirements.txt') as f:
    for line in f:
      li = line.strip()
      if not li.startswith('#'):
        requirements.append(li)
  return requirements

# }}}


# Setup package {{{

def setup_package():
  '''
  Set up the package.
  '''

  metadata = dict(
      name='complot',
      version=VERSION,
      author=__author__,
      author_email=__email__,
      url='https://github.com/marromlam/complot.git',
      download_url='https://github.com/marromlam/complot.git',
      install_requires=install_requirements(),
      python_requires='>=3.5',
      license=__license__,
      description='Statistical and plotting tools.',
      long_description=open('README.rst').read() + "\n\n" + __license__,
      long_description_content_type = 'text/x-rst',
      platforms=['Linux', 'macOS', 'Windows'],
      keywords='statistics plotting',
      include_package_data=True,
      # package_dir={'complot': 'complot'},
      packages=['complot'],
  )

  create_version_file()
  setuptools.setup(**metadata)


if __name__ == '__main__':
  setup_package()

# }}}


# vim:foldmethod=marker

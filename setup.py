#!/usr/bin/env python

from setuptools import find_packages, setup


PACKAGE_NAME = 'cenaming'


def get_requirements(requirement_file):
    requirements = list(open(requirement_file).read().strip().split('\r\n'))
    return requirements


setup(name=PACKAGE_NAME,
      packages=find_packages(PACKAGE_NAME),
      package_data={
          '': ['*.txt', '*.sql', '*.json'],
      },
      include_package_data=True,
      version='0.0.1',
      description='Company legal name normalization and shortening.',
      url='https://github.com/portfoliome/cenaming',
      author='Philip Martin',
      author_email='philip.martin@censible.co',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.5',
          'Topic :: Utilities'
      ],
      keywords='companies finance names',
      tests_require=get_requirements('requirements-test.txt'),
      extras_require={
          'develop': get_requirements('requirements-dev.txt'),
          'test': get_requirements('requirements-test.txt')
      },
      zip_safe=False)

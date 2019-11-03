# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in chdnextgr/__init__.py
from chdnextgr import __version__ as version

setup(
	name='chdnextgr',
	version=version,
	description='Greek country support for ERP Next',
	author='ChD Computers',
	author_email='chdcomputers@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-datagr',
	version=version,
	description="Theme for data.grcity.us",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Dave Brondsema',
	author_email='dave@brondsema.net',
	url='http://data.grcity.us',
	license='Apache License 2.0',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.datagr'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	datagr=ckanext.datagr.plugin:DataGrThemePlugin
	""",
)

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'bagit-K - Create bag for a directory of kirtas digitized books',
	'author': 'Nick Ruest',
	'url': 'https://github.com/ruebot',
	'author_email': 'ruestn@mcmaster.ca',
	'version': '0.1',
	'install_requirements': 'bagit',
	'name': 'bagit-K'
}

setup(**config)

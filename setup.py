try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'bagitk - Create bag for a directory of kirtas digitized books',
	'author': 'Nick Ruest', 'Matt McCollow',
	'url': 'https://github.com/scds/bagit-k',
	'author_email': 'ruestn@mcmaster.ca', 'mccollo@mcmaster.ca',
	'version': '0.1',
	'install_requirements': 'bagit',
	'name': 'bagitk'
}

setup(**config)

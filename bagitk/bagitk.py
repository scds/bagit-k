#!/usr/bin/env python

# BagIt-K script - Generate a BagIt package from Kirtas scanner data
# Author: Matt McCollow <mccollo@mcmaster.ca>
# Author: Nick Ruest <ruestn@mcmaster.ca>

from sys import exit, argv
from os import listdir
from os.path import exists, dirname
from xml.dom import minidom
import bagit

# Use these to customize BagIt metadata
SOURCE_ORGANIZATION = ''
ORGANIZATION_ADDRESS = ''
CONTACT_NAME = ''
CONTACT_PHONE = ''
CONTACT_EMAIL = ''

class BagItK(object):
	def __init__(self):
		this.scriptname = argv[0]
		this.src = argv[1]
		this.dest = argv[2]
	
	# Validate a BagIt folder structure
	def validate(self, dir):
		if not exists(dir):
			_log_error("Folder " + dir + " does not exist.")
			exit(1)
		look_for = ['OCR', 'PDF', 'IMAGES', 'METADATA']
		for folder in look_for:
			target = dir + os.sep + folder
			if not exists(target):
				_log_error("Folder " + target + " does not exist.")
				exit(1)
			if listdir(target).__len__() < 1:
				_log_error("Folder " + target + " is empty.")
				exit(1)
		return True
	
	# Log an error to file
	def _log_error(self, msg):
		try:
			log = open('bagitk.log', 'w+')
			log.write(msg)
			log.close()
		except IOError:
			print this.scriptname + " has encountered an error but is unable to open log file for writing. Check that you have write permissions in the current folder."

	# Get the value of dc.title from xmlfile
	def _get_title(self, xmlfile):
		DCNS = "http://purl.org/dc/elements/1.1/"
		dom = minidom.parse(xmlfile)
		for node in dom.getElementsByTagNameNS(DCNS, 'title'):
			title = node.firstChild.data.strip("\n\t ")
		return title
	
	# Execute bagit.py
	def bagitk(self):
		bag = bagit.Bag(
			this.dest,
			{
				'Source-Organization': SOURCE_ORGANIZATION,
				'Organization-Address': ORGANIZATION_ADDRESS,
				'Contact-Name': CONTACT_NAME,
				'Contact-Phone': CONTACT_PHONE,
				'Contact-Email': CONTACT_EMAIL,
				'External-Description': this.dest + '-' + this._get_title(this.dest + os.sep + "foo_DC.xml"),
				'External-Identifier': this.dest
			}
		)

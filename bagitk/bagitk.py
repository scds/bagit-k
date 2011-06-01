#!/usr/bin/env python

# BagIt-K script - Generate a BagIt package from Kirtas scanner data
# Author: Matt McCollow <mccollo@mcmaster.ca>
# Author: Nick Ruest <ruestn@mcmaster.ca>

from sys import exit, argv
from os import listdir
from os.path import exists, dirname, basename
from xml.dom import minidom
import bagit

# Use these to customize BagIt metadata
SOURCE_ORGANIZATION = ''
ORGANIZATION_ADDRESS = ''
CONTACT_NAME = ''
CONTACT_PHONE = ''
CONTACT_EMAIL = ''

# This is the indicator for volume number in a folder name
# For example: the V in 12345678V1 to indicate Volume 1
VOLUME_INDICATOR = 'V'

class OCLC(object):
	def __init__(self, number, volume=None);
		self.number = number
		self.volume = volume

class BagItK(object):
	def __init__(self, src, dest):
		self.src = src
		self.dest = dest
	
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
			if len(listdir(target)) < 1:
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
			print "BagItK has encountered an error but is unable to open log file for writing. Check that you have write permissions in the current folder."

	# Get the value of dc.title from xmlfile
	def _get_title(self, xmlfile):
		DCNS = "http://purl.org/dc/elements/1.1/"
		dom = minidom.parse(xmlfile)
		for node in dom.getElementsByTagNameNS(DCNS, 'title'):
			title = node.firstChild.data.strip("\n\t ")
		return title
	
	# Get the OCLC number from the source folder
	def _get_oclc(self):
		if self.src.find(VOLUME_INDICATOR) > -1:
			parts = self.src.split(VOLUME_INDICATOR)
			oclc = OCLC(parts[0], parts[1])
		else:
			oclc = OCLC(basename(self.src))
		self.oclc = oclc
		
	# Execute bagit.py
	def bagitk(self):
		bag = bagit.Bag(
			self.dest,
			{
				'Source-Organization': SOURCE_ORGANIZATION,
				'Organization-Address': ORGANIZATION_ADDRESS,
				'Contact-Name': CONTACT_NAME,
				'Contact-Phone': CONTACT_PHONE,
				'Contact-Email': CONTACT_EMAIL,
				'External-Description': self.dest + '-' + self._get_title(self.dest + os.sep + self.oclc + "_DC.xml"),
				'External-Identifier': self.dest
			}
		)

def usage():
	print "Produces a BagIt package from Kirtas data folder."
	print "Usage: python bagitk.py SRC DEST"

if __name__ == "__main__":
	if len(argv) < 3:
		usage()
		exit(1)
	bk = BagItK(argv[1], argv[2])
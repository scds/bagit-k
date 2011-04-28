#!/usr/bin/python

import bagit
import sys

bagit-k_HOME = /home/nruest/dc1/dc2/Digital-Collections/archival-objects/Kirtas/books-completed/Books

mydir = mydir() #iterate through each top level directory in books folder and read foldername

os.fetchdir()

os.chdir()

def listBooks()
	os.listdir(bagit-K_HOME)

def validateBooks()

source-organization = 'McMaster University'
organization-address = '1280 Main St. West Mills Memorial Library, Hamilton ON L8S 4L6'
contact-name = 'Nick Ruest'
contact-email = 'ruestn@mcmaster.ca'
contact-phone = '+1 905 525 9140 x21276'
internal-sender-description = #Read from Metadata directory - open oclc#_DC.xml and print title


internal-sender-identifier = #folder name

bag = bagit.make_bag(
		mydir, 
		{'Source-Organization': source-organization},
		{'Organization-Address': organization-address}, 
		{'Contact-Name': contact-name},
		{'Contact-Email': contact-email}, 
		{'Contact-Phone': contact-phone},
		{'Internal-sender-identifier': internal-sender-identifier},
		{'Internal-Sender-Description': internal-sender-description}
)



import urllib2
import json
import sys

#General functions used for Saks Api

def getResource(url):
	try:
		# get the content from api starting at page 1
		json_page = urllib2.urlopen(url)

		# parse the json into python objects
		ustr_to_load = unicode(json_page.read(), 'latin-1')
		parsed = json.loads(ustr_to_load)
	
		return parsed
	except Exception, e:
		print e
		return None

def printMainHttpError():
	sys.exit("Content could not be retrieved from Saks Api.\n\n Stopping the process.\n\nNote: 403 means your api key is not good")


import constants
import saks_api_utils

print ">>> Events download and load process started ..."

parsed = saks_api_utils.getResource(constants.content_events_url + constants.api_key_events)

if parsed == None:
	saks_api_utils.printMainHttpError

resource = parsed['resource']

print constants.content_events_url
print resource['stores']['store']['name']

print ">>> Events downloaded and loaded with success!"



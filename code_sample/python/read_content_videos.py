import constants
import saks_api_utils

print ">>> Videos download and load process started ..."

parsed = saks_api_utils.getResource(constants.content_video_url + constants.api_key_events)

if parsed == None:
	saks_api_utils.printMainHttpError

resource = parsed['resource']

print constants.content_video_url
print resource['videos'][0]

print ">>> Videos downloaded and loaded with success!"



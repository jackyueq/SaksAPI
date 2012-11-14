import constants
import saks_api_utils

#
#Note: This sample is a sequencial product catalog data extraction
#For more performatic example, look at the paralel product catalog extraction sample code
#

print ">>> Product catalog download and load process started ..."

parsed = saks_api_utils.getResource(constants.product_catalog_by_page_url + "1" + constants.api_key_product)

if parsed == None:
	saks_api_utils.printMainHttpError

resource = parsed['resource']
#Do something with your content, save it in your DB, extract the data you want, etc
#For the example, I am gonna print the product code only

print constants.product_catalog_by_page_url + "1"
print resource[0]['product_code']

counter = 1
# iterate through every product page
link_to_next_page = parsed['linkRepresentation']
while link_to_next_page != None:

	next_page = link_to_next_page['next']['href']
	parsed = saks_api_utils.getResource(next_page + constants.api_key_product)
	resource = parsed['resource']

	#Do something with your content, save it in your DB, extract the data you want, etc
	#For the example, I am gonna print the product code only
	print next_page
	#If you want see all product keys-values just remove the ['product_code'] below
	#For now this test the product code is all we need
	print resource[0]['product_code']

	#Get the url to the next page
	link_to_next_page = parsed['linkRepresentation']

	#Note: I don't want to go over the entire catalog so get off from loop at 5th iteration
	counter += 1
	if counter == 5:
		break

print ">>> Product catalog downloaded and loaded with success!"



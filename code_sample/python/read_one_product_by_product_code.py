import constants
import saks_api_utils

print ">>> One Product by product code download and load process started ..."

parsed = saks_api_utils.getResource(constants.product_catalog_by_page_url + "1" + constants.api_key_product)

if parsed == None:
	saks_api_utils.printMainHttpError

resource = parsed['resource']

print constants.product_catalog_by_page_url + "1"
product_code = resource[0]['product_code']
print product_code

parsed = saks_api_utils.getResource(constants.product_catalog_url + product_code + constants.api_key_product)

#Do something with your content, save it in your DB, extract the data you want, etc
#For the example, I am gonna print some values
print parsed['description'], parsed['brand_name']

print ">>> One Product by product code downloaded and loaded with success!"



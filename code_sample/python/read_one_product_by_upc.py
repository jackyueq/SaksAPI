import constants
import saks_api_utils

print ">>> One Product by upc download and load process started ..."

parsed = saks_api_utils.getResource(constants.product_catalog_by_page_url + "1" + constants.api_key_product)

if parsed == None:
	saks_api_utils.printMainHttpError

resource = parsed['resource']

print constants.product_catalog_by_page_url + "1"
#Note: I am assuming that the first product in the array has variants(upcs)
#If not, this will blow up
upc_code = resource[0]['variants'][0]['upc']
print upc_code

parsed = saks_api_utils.getResource(constants.product_catalog_by_variant_url + upc_code + constants.api_key_product)

#Do something with your content, save it in your DB, extract the data you want, etc
#For the example, I am gonna print the product code only
print parsed['description'], parsed['brand_name']

print ">>> One Product by upc downloaded and loaded with success!"



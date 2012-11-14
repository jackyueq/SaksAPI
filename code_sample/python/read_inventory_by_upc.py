import constants
import saks_api_utils

print ">>> Inventory by upc download and load process started ..."

parsed = saks_api_utils.getResource(constants.product_catalog_by_page_url + "1" + constants.api_key_product)

if parsed == None:
	saks_api_utils.printMainHttpError

resource = parsed['resource']

print constants.product_catalog_by_page_url + "1"
#Note: I am assuming that the first product in the array has variants(upcs)
#If not, this will blow up
upc_code = resource[0]['variants'][0]['upc']
print upc_code

parsed = saks_api_utils.getResource(constants.inventory_by_variant_url + upc_code + constants.api_key_inventory)

#Do something with your content, save it in your DB, extract the data you want, etc
#For the example, I am gonna print some values
print parsed['upc'], parsed['in_stock'], parsed['on_order']

print ">>> Inventory by upc downloaded and loaded with success!"



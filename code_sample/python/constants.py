#Constants used in the python example

#api_key, note: You will need to add your own api key in the constants below
api_key = "?api_key="
api_key_product = api_key + "[Your api key goes here]"
api_key_inventory = api_key + "[Your api key goes here]"
api_key_events = api_key + "[Your api key goes here]"

unsecure_protocol = "http://"
server_name = "api.saks.com/"
api_version = "v2/"

full_unsecure_url = unsecure_protocol + server_name + api_version

#product catalog main url
product_catalog_url = full_unsecure_url + "products/"
product_catalog_by_variant_url = full_unsecure_url + "products/variant/"
product_catalog_by_page_url = full_unsecure_url + "products/page/"

inventory_by_product_code_url = full_unsecure_url + "inventory/product/"
inventory_by_variant_url = full_unsecure_url + "inventory/variant/"

content_video_url = full_unsecure_url + "content/videos"
content_events_url = full_unsecure_url + "content/events"


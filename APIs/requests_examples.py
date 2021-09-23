import requests
import json
from pprint import pprint

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/B240JT")
# print(post_codes_req.status_code)
# print(post_codes_req.headers)
# print(post_codes_req.content)
# print(post_codes_req.json())

json_body = json.dumps({"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]})
headers = {"Content-Type": 'application/json'}

multi_postcode_req = requests.post("https://api.postcodes.io/postcodes", headers = headers, data = json_body)
pprint(multi_postcode_req.json())


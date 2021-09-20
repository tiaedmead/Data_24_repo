import requests
from pprint import pprint

request_bbc = requests.get("https://www.bbc.com/")
pprint(request_bbc.text)

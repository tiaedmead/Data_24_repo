import requests
from pprint import pprint

# cat_facts = requests.get("https://catfact.ninja/fact")
# pprint(cat_facts.json())
#
# bored = requests.get("https://www.boredapi.com/api/activity")
# pprint(bored.json())

dog_images = requests.get("https://dog.ceo/api/breeds/image/random")
pprint(dog_images.json())

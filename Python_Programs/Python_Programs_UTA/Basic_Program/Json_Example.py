import requests

#quiz api google search

r = requests.get("https://opentdb.com/api.php?amount=1&category=12&type=multiple")

print(r.status_code) # printing status_code

print(r.text) #  text

# work with json

import json

question = json.loads(r.text)
print(question)  # prints the json code of the site

type(question)

import pprint
pprint.pprint(question)



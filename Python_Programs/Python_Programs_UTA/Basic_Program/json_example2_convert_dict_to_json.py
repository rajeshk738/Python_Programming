import json
import pprint


# converting a dictionary in python to json object

person = {'Name': 'Rajesh', 'Age': 23}

person_json = json.dumps(person)

pprint.pprint(person_json)

type(person_json)

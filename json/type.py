import json


json_open = open('template.json', 'r')
json_data = json.load(json_open)
print(type(json_data))

molecule = json_data.get('molecule')
if type(molecule) is dict:
    print('molecule type is dict')

charge = json_data.get("molecule").get("charge")
if type(charge) is list:
    print('charge type is list')

print(charge)
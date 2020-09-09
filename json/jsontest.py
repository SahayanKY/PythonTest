import json

json_open = open('sample.json', 'r')
json_data = json.load(json_open)

print('gaussian_chart' not in json_data)
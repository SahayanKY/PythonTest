import json

json_open = open('template.json', 'r')
json_data = json.load(json_open)

genecpdict = json_data['plan'][0]['genecp']

atomlist = ['C','H','H','H','H','Ni']
elementStrSet = set(atomlist)

genecpdict = { element : genecpdict[element] for element in genecpdict if element in elementStrSet }
print(genecpdict)
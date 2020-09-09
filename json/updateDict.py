import sys
import json

jsonOpen = open('template.json', 'r')
jsonData = json.load(jsonOpen)

print(type(jsonData['molecule']))

for i in range(len(jsonData['plan'])):
    planData_i = {}
    planData_i.update(jsonData['generalplan'])
    planData_i.update(jsonData['plan'][i])

    print(i)
    print(planData_i)
    print('-----------------')
    #rootsection = '#' + (str = planData_i.get('logdetail'); str if str is None else 'p')

print(jsonData['generalplan'])
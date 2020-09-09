import sys
import json

jsonOpen = open('template.json', 'r')
jsonData = json.load(jsonOpen)
print(type(jsonData))
print('start')
for i in range(len(jsonData['plan'])):
    planData_i = jsonData['plan'][i]
    getPlanDataValue = lambda key : planData_i[key] if key in planData_i else jsonData['generalplan'][key]

    jobType = getPlanDataValue('jobtype')
    print(jobType)

print('end')


print(jsonData['hoge'])
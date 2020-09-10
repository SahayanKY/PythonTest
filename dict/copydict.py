import copy

dict1 = {
    "a":{
        "a1" : 1,
        "a2" : 2
    },
    "b":1
}

dict2 = copy.deepcopy(dict1)

dict1['a']['a1'] = 4
dict1['b'] = -1

print(dict2)
#dict1.copy()
#{'a': {'a1': 4, 'a2': 2}, 'b': 1}

#copy.deepcopy(dict1)
#{'a': {'a1': 1, 'a2': 2}, 'b': 1}
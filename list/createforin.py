def calc(c):
    return 1 + c%2

charge = [0,1,2]
multi = [ calc(c) for c in charge ]

print('charge',charge)
print('multi',multi)

map = [ [c,calc(c)] for c in charge ]
print('map',map)
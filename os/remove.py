import os

filepath = 'hogehoge.txt'
if os.path.exists(filepath):
    os.remove(filepath)
else:
    print('file doesnt exist.')
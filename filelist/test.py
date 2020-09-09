import os

path = './testdir'

filelist = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print(filelist)
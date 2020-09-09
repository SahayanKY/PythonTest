import pathlib
import glob
import os

path = pathlib.Path('.')

filelist = list(path.glob('../filelist/**/*.gjf'))
print(filelist)
print(str(filelist[0]))



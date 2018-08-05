from os import walk
import os

f = []

DIR_NAME = os.path.dirname(__file__)

PATH = os.path.join(DIR_NAME, '..', 'real_data')

for (dirpath, dirnames, filenames) in walk(PATH):
    f.extend(filenames)
    break

k = [txt for txt in f if '.txt' in txt]
print(k)
# filedemo_05.py
import os, glob

dir = 'C:\Work\github\python\day06'
os.chdir(dir)
filter_list = glob.glob('*.txt')
for file in filter_list:
    print(file)
# files = os.listdir(dir)
# for file in files:
#     if file.
#     print(file)
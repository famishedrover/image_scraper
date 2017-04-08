import os 
from os.path import join 
from sys import argv
folder  = ''
try :
	folder = argv[1]
except :
	print 'No path given'
	exit()

dirs = os.listdir(folder)

for d in dirs :
	print 'Converting %s '%d
	os.rename(join(folder ,d), join(folder , d + '.jpg'))
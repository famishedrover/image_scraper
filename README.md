# Requirements :
	Python 2.x
	shutil
	urllib2
	BeautifulSoup


python main.py [savelocation] [url]
Default savelocation 	: Current Working Directory (CWR)
Default url 			: 'https://en.wikipedia.org/wiki/Image'

To save the images at say , myoutput , 
1. ensure myoutput does not already exist
2. If it exists then myoutput0 is created. (and so on)
4. if only directory name is supplied as first argument then new directory in the CWR 
	is created.
3. If directory path is invalid , Current Working Directory is selected with 
	output directory name as 'output'


Script to download all images from a given url.

URL can be supplied from the cli 


Example : 
	1. python main.py /Users/famishedrover/Deskasdftop/myoutput

	Since Deskasdftop does not exist current working directory is selected 
	with output folder name as output 

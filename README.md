# Requirements :
	Python 2.x
	shutil
	urllib2
	BeautifulSoup


python main.py [savelocation]/[dirname] [url]


eg. python main.py /Users/famishedrover/Desktop/mydir www.somewebsite/imageurl

[savelocation] 	: Wherever you want to save the retrieved image.
[dirname] 		: Name of directory to be created.
[url] 			: url from which images are to be retieved.

Default savelocation 	: Current Working Directory (CWR)
Default url 			: 'https://en.wikipedia.org/wiki/Image'

To save the images at say , myoutput , 
1. ensure myoutput does not already exist
2. If it exists then myoutput0 is created. (and so on)
3. if only directory name is supplied as first argument then new directory in the CWR 
	is created.
4. If directory path is invalid , Current Working Directory is selected with 
	output directory name as directory name supplied , if not given it is changed to 
	default name 'output'
5. Saving at home directory is denied.


Script to download all images from a given url.

URL can be supplied from the cli 


Example : 
	1. python main.py /Users/famishedrover/Deskasdftop/myoutput

	Since Deskasdftop does not exist current working directory is selected 
	with output folder name as output 
	
	2. python main.py /
	Since home dir is tried , save location is changed to ./ and ,
	since no dirname is supplied 
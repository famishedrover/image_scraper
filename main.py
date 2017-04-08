from bs4 import BeautifulSoup 
import urllib2 
import shutil
import requests
from urlparse import urljoin
import sys 
from sys import argv
import time
import os 

def create_output(dirname  , saveloc = './') :
	print 'Given save location ',saveloc
	

	try :
		dirs = os.listdir(saveloc)
	except :
		print 'Supplied Save Location NOT FOUND. ',
		print 'Save Location set to Current Working Directory'
		print 'Directory name set to Default - output'
		dirname = 'output'
		dirs = os.listdir('./')

	originaldirname = dirname
	cnt = 0
	num = str(cnt)
	while dirname in dirs :
		# print dirname ,' exists.',
		dirname = originaldirname + num
		cnt += 1
		num = str(cnt)

	try :
		os.mkdir(saveloc + dirname)
	except:
		os.mkdir('./'+ dirname)
		print 'Save Location set to Current Working Directory'
	
	print dirname ,'named Directory created.',
	print ' Images will be saved here.'
	#returning outut dir full path 
	return saveloc + dirname


def get_dir() :
	currdir = os.getcwd()
	print 'Current Directory :' , currdir



def make_soup (url) : 
	# to prevent 403 : FORBIDDEN error.
	req = urllib2.Request(url , headers = {'User-Agent' : 'Magic Browser'})

	html = urllib2.urlopen(req)
	return BeautifulSoup(html , 'html.parser')


def get_images(url , saveloc = './') :
	soup = make_soup(url)
	#found all images html.
	images = [img for img in soup.findAll('img')]
	print (len(images) , 'Images Found!')
	# for i in images :
	# 	print i


	get_dir()
	dirpath = '/'.join(saveloc.split('/')[:-1]) + '/'
	dirname = saveloc.split('/')[-1]
	savedir = create_output(dirname , dirpath)



	print ('Downloading into %s directory...'%savedir)



	image_links = [eachimg.get('src') for eachimg in images]

	for eachimg in image_links :
		try :
			#Finding the name of the file. 
			filename = eachimg.strip().split('/')[-1].strip()

			#src tag
			src = urljoin(url , eachimg)

			print ('Retreiving ' + filename)
			r = requests.get(src , stream = True)
			time.sleep(1)		#delay

			#saving.
			with open(savedir + '/' + filename, 'wb') as of :
				shutil.copyfileobj(r.raw,of)


			#below method dosen't work.
			# with open(filename , 'wb') as of :
			# 	for chunk in r.iter_content(chunk_size = 256) :
			# 		fd.write(chunk)

		except KeyboardInterrupt :
			print 'KeyboardInterrupt' 
			exit()

		except :
			print ('Error occured , Continuing ...')
	print ('Completed!')





if __name__ == '__main__' :
	try :
		url = argv[2]
	except :
		url = 'https://en.wikipedia.org/wiki/Image'

	try :
		dirpath = argv[1]
	except :
		currdir = os.getcwd()
		dirpath = currdir + '/output'


	get_images(url , saveloc = dirpath)



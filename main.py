from bs4 import BeautifulSoup 
import urllib2 
import shutil
import requests
from urlparse import urljoin
import sys 
import time


def make_soup (url) : 
	# to prevent 403 : FORBIDDEN error.
	req = urllib2.Request(url , headers = {'User-Agent' : 'Magic Browser'})

	html = urllib2.urlopen(req)
	return BeautifulSoup(html , 'html.parser')


def get_images(url) :
	soup = make_soup(url)
	#found all images html.
	images = [img for img in soup.findAll('img')]
	print (len(images) , 'Images Found!')
	# for i in images :
	# 	print i


	print ('Downloading into working directory...')
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
			with open(filename, 'wb') as of :
				shutil.copyfileobj(r.raw,of)


			#below method dosen't work.
			# with open(filename , 'wb') as of :
			# 	for chunk in r.iter_content(chunk_size = 256) :
			# 		fd.write(chunk)



		except :
			print ('Error occured , Continuing ...')
	print ('Completed!')



if __name__ == '__main__' :
	url = 'https://en.wikipedia.org/wiki/Image'
	get_images(url)








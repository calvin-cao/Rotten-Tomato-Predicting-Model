
import urllib.request, json
import re
import time
import requests
import os
from colorama import Fore, Back, Style
import math


### Step 0a: Creating the working folder in the directory ###
PATH = input('Enter desired file path: ')
if len(PATH) < 1:
    PATH = 'C:/Local'

if not os.path.exists(PATH + '/RT/'):
	os.makedirs(PATH + '/RT/')


### Step 0b: Defining the functions ###

def grabURLs(url,filename,pagenumber):
	pageNum = int(pagenumber)
	for i in range(1, pageNum + 1):
		if i == 1:
			pageLink = url
		else:
			pageLink = url + '&page=' + str(i)
		for ii in range(5):
			try:
				with urllib.request.urlopen(pageLink) as url1:
					data=json.loads(url1.read().decode())
				break
			except Exception as e:
				log1.write(filename + ': Page ' + i + ' - Failed attempt ' + ii + '\n')
				time.sleep(2)
		data_str = str(data)
		url_location = [m.start() for m in re.finditer("'url':", data_str)]
		for x in url_location:
			url_start = x
			url_end = data_str.find(',', url_start)
			URL = data_str[url_start + 8 : url_end - 1]
			movie_url = 'www.rottentomatoes.com' + URL
			if not movie_url in A:
				A.append(movie_url)
			else:
				continue
		log1.write(filename + ': Page ' + i + ' - Done' + '\n')
		print(Style.RESET_ALL)
	return


def getHTML(partx):
	with open(PATH + '/RT/RT_All_URLs_Gen1_12_Part_' + str(partx) + '.txt', 'r') as myfile:
		urls = myfile.read()
	urls_ls = urls.split('\n')
	c = 0
	failed_ls = []
	for x in urls_ls:
		c = c + 1
		log2.write(str(c) + '. ' + x[25:] + ' - ')
		for i in range(5):
			page = None
			pagetext = None
			fh = None
			log2.write('Attempt ' + str(i+1) + ': ')
            
			try:
				page = requests.get('https://' + x)
				if not page:
					log2.write('Page request error' + '\n')
					time.sleep(2)
					continue
				pagetext = page.text
				if not pagetext:
					log2.write('Page decode error' + '\n')
					time.sleep(0.5)
					continue
				log2.write('Good page response, ')
			except:
				log2.write('Failed page acquisition' + '\n')
				time.sleep(1)
				continue
            
			try:
				fh = open(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html', 'w')
				if not fh:
					log2.write('File handle assignment error' + '\n')
					time.sleep(0.5)
					continue
			except:
				log2.write('File handle error' + '\n')
				time.sleep(0.5)
				continue
            
			try:
				fh.write(pagetext)
				fh.close()
				log2.write('Good file, ')
			except:
				fh.close()
				log2.write('File writing error' + '\n')
				if os.path.exists(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html'):
					os.remove(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html')
					time.sleep(1)
					continue
				else:
					time.sleep(1)
					continue
                
			log2.write('Done' + '\n')
			time.sleep(0.1)
			break
		if not os.path.exists(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html'):
			failed_ls.append(x)
			continue
	fa = open(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/Failed_list_Part_' + str(partx) + '.txt', 'w')
	for n in failed_ls:
		fa.write(str(n) + '\n')
	return




### Step 1: Loop over all the webpages to  ###
time.sleep(1)
print(Fore.LIGHTGREEN_EX + 'Starting Step 1')
print(Style.RESET_ALL)
time.sleep(1)


URLs = ['https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=1&certified&sortBy=release&type=dvd-streaming-all',
        'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=2&certified&sortBy=release&type=dvd-streaming-all',
        'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=4&certified&sortBy=release&type=dvd-streaming-all',
        'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=5&certified&sortBy=release&type=dvd-streaming-all',
        'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=6&certified&sortBy=release&type=dvd-streaming-all',
        'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=8&certified&sortBy=release&type=dvd-streaming-all',
        'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=9&certified&sortBy=release&type=dvd-streaming-all',
        'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=10&certified&sortBy=release&type=dvd-streaming-all',
        'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=11&certified&sortBy=release&type=dvd-streaming-all',
        'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=13&certified&sortBy=release&type=dvd-streaming-all',
        'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=18&certified&sortBy=release&type=dvd-streaming-all',
        'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=14&certified&sortBy=release&type=dvd-streaming-all']

#Genre          Genre_id
#Action         	1
#Animation      	2
#Art&Foreign    	4
#Classics	        5
#Comedy	       		6
#Documentary    	8
#Drama          	9
#Horror         	10
#Kids&Family    	11
#Mystery        	13
#Romance        	18
#Scifi&Fantasy		14


Genres = ['Action', 
          'Animation', 
          'Art&Foreign', 
          'Classics', 
          'Comedy', 
          'Documentary', 
          'Drama', 
          'Horror', 
          'Kids&Family', 
          'Mystery', 
          'Romance', 
          'Scifi&Fantasy']

Pages = []
A = []

for url in URLs:
    for ii in range(5):
        try:
            with urllib.request.urlopen(url) as url1:
                data=json.loads(url1.read().decode())
            break
        except Exception as e:
            print('Failed attempt ',ii)
            time.sleep(2)
    
    data_str = str(data)
    count_loc = [m.start() for m in re.finditer("'total':", data_str)]
    for x in count_loc:
        count_start = x
        count_end = data_str.find('},', count_start)
        total_movies = math.ceil(int(data_str[count_start + 9 : count_end])/32)
        Pages.append(total_movies)


log1 = open(PATH + '/RT/log_grabURLs.txt', 'w')

for i in range(len(URLs)):
    grabURLs(URLs[i],Genres[i],Pages[i])
    
log1.close()

print('List length: ' + str(len(A)) + '\n')
time.sleep(2)
print(Fore.LIGHTGREEN_EX + 'Step 1 completed, proceed in 3 seconds...')
print(Style.RESET_ALL)
time.sleep(3)
print(Fore.LIGHTGREEN_EX + 'Step 2 starts')
print(Style.RESET_ALL)
time.sleep(1)

### Step2:  ###
print('running...' + '\n')
r = 0
for x in range(0,len(A),600):
	r += 1
	fh = open(PATH + '/RT/RT_All_URLs_Gen1_12_Part_' + str(r) + '.txt','w')
	for s in A[x : x + 600]:
		fh.write(str(s) + '\n')
	fh.close()
#if A:
#	del A


print(Fore.LIGHTGREEN_EX + 'Step 2 completed, proceed in 3 seconds...')
print(Style.RESET_ALL)
time.sleep(3)
print(Fore.LIGHTGREEN_EX + 'Step 3 starts')
print(Style.RESET_ALL)
time.sleep(1)

### Step 3: Collect main pages for each movie on the URL list (.html) ###
	
# RT_All_Gen1_12_Movie_Page_Sources_HTML
if not os.path.exists(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/'):
	os.makedirs(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/')


log2 = open(PATH + '/RT/log_getHTML.txt', 'a')

counter = math.ceil(len(A)/600)
for i in range(1, counter + 1):
	getHTML(i)

log2.close()

print(Fore.LIGHTGREEN_EX + 'Process finished')
print(Style.RESET_ALL)
exit()

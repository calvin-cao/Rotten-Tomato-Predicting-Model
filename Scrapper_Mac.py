import urllib.request, json
import re
import time
import requests
import os
from colorama import Fore, Back, Style
from multiprocessing import Process, Manager

PATH = input('Enter desired file path: ')
# /Users/CalvinCao/Desktop

if not os.path.exists(PATH + '/RT/'):
	os.makedirs(PATH + '/RT/')
time.sleep(1)
print(Fore.LIGHTGREEN_EX + 'Starting Step 1')
print(Style.RESET_ALL)
time.sleep(1)

### Step 1:  ###
def run1(url,filename,pagenumber):
	pageNum = int(pagenumber)
	for i in range(1, pageNum + 1):
		print(filename + ': '+ 'Page', i)
		if i == 1:
			pageLink = url
		else:
			pageLink = url + '&page=' + str(i)
		for ii in range(5):
			try:
				with urllib.request.urlopen(pageLink) as url1:
					data=json.loads(url1.read().decode())
			except Exception as e:
				print('failed attept',ii)
				time.sleep(2)
		data_str = str(data)
		url_location = [m.start() for m in re.finditer("'url':", data_str)]
		# print(url_location)
		for x in url_location:
			url_start = x
			url_end = data_str.find(',', url_start)
			URL = data_str[url_start + 8 : url_end - 1]
			movie_url = 'www.rottentomatoes.com' + URL
			if not movie_url in A:
				A.append(movie_url)
			else:
				continue
		print(Fore.GREEN + 'Done')
		print(Style.RESET_ALL)
	return

U = ['https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=1&certified&sortBy=release&type=dvd-streaming-all','https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=2&certified&sortBy=release&type=dvd-streaming-all','https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=4&certified&sortBy=release&type=dvd-streaming-all','https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=5&certified&sortBy=release&type=dvd-streaming-all','https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=6&certified&sortBy=release&type=dvd-streaming-all','https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=8&certified&sortBy=release&type=dvd-streaming-all','https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=9&certified&sortBy=release&type=dvd-streaming-all','https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=10&certified&sortBy=release&type=dvd-streaming-all','https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=11&certified&sortBy=release&type=dvd-streaming-all','https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=13&certified&sortBy=release&type=dvd-streaming-all','https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=18&certified&sortBy=release&type=dvd-streaming-all','https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=14&certified&sortBy=release&type=dvd-streaming-all',]

N = ['Action', 'Animation', 'Art&Foreign', 'Classics', 'Comedy', 'Documentary', 'Drama', 'Horror', 'Kids&Family', 'Mystery', 'Romance', 'Scifi&Fantasy']

P = [97, 16, 69, 47, 156, 54, 258, 53, 31, 95, 54, 50]
# P = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

MNG = Manager()
A = MNG.list()
Processes = []
for i in range(10):
	p = Process(target = run1, args = (U[i],N[i],P[i]))
	Processes.append(p)
	p.start()
for p in Processes:
	p.join()

print('List length: ' + str(len(A)) + '\n')
time.sleep(2)
print(Fore.LIGHTGREEN_EX + 'Step 1 completed, proceed in 3 seconds...')
print(Style.RESET_ALL)
time.sleep(3)
print(Fore.LIGHTGREEN_EX + 'Step 2 starts')
time.sleep(1)

### Step2:  ###
print('running...')
r = 0
for x in range(0,len(A),600):
	r += 1
	fh = open(PATH + '/RT/RT_All_URLs_Gen1_12_Part_' + str(r) + '.txt','w')
	for s in A[x : x + 600]:
		fh.write(str(s) + '\n')
	fh.close()
if A:
	del A

print(Fore.LIGHTGREEN_EX + 'Step 2 completed, proceed in 3 seconds...')
print(Style.RESET_ALL)
time.sleep(3)
print(Fore.LIGHTGREEN_EX + 'Step 3 starts')
print(Style.RESET_ALL)
time.sleep(1)

### Step 3: Collect main pages for each movie on the URL list (.html) ###
def run4(partx):
	import os
	import time
	import requests
	from colorama import Fore, Back, Style
	with open(PATH + '/RT/RT_All_URLs_Gen1_12_Part_' + str(partx) + '.txt', 'r') as myfile:
		urls = myfile.read()
	urls_ls = urls.split('\n')
	c = 0
	failed_ls = []
	for x in urls_ls:
		c = c + 1
		print(str(c) + '. ' + x[25:] + ':')
		for i in range(5):
			page = None
			pagetext = None
			fh = None
			print(Fore.BLUE + 'Attempt ' + str(i+1) + ':')
			print(Style.RESET_ALL)
			try:
				page = requests.get('https://' + x)
				if not page:
					print(Fore.LIGHTYELLOW_EX + '  Page request error')
					print(Style.RESET_ALL)
					time.sleep(2)
					continue
				pagetext = page.text
				if not pagetext:
					print((Fore.LIGHTYELLOW_EX + '  Page decode error'))
					print(Style.RESET_ALL)
					time.sleep(0.5)
					continue
				print(Fore.GREEN + '  Good page response')
				print(Style.RESET_ALL)
			except:
				print(Fore.LIGHTYELLOW_EX + '  Failed page acquisition')
				print(Style.RESET_ALL)
				time.sleep(1)
				continue
			try:
				fh = open(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html', 'w')
				if not fh:
					print(Fore.LIGHTYELLOW_EX + '  File handle assignment error')
					print(Style.RESET_ALL)
					time.sleep(0.5)
					continue
			except:
				print(Fore.LIGHTYELLOW_EX + '  File handle error')
				print(Style.RESET_ALL)
				time.sleep(0.5)
				continue
			try:
				fh.write(pagetext)
				fh.close()
				print(Fore.GREEN + '  Good file')
				print(Style.RESET_ALL)
			except:
				fh.close()
				print(Fore.LIGHTYELLOW_EX + '  File writing error')
				print(Style.RESET_ALL)
				if os.path.exists(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html'):
					os.remove(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html')
					time.sleep(1)
					continue
				else:
					time.sleep(1)
					continue
			print(Fore.LIGHTGREEN_EX + '  Done')
			print(Style.RESET_ALL)
			time.sleep(0.1)
			break
		if not os.path.exists(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html'):
			failed_ls.append(x)
			print(Fore.LIGHTRED_EX + 'FAILED: ' + x[25:])
			print(Style.RESET_ALL)
			continue
	fa = open(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/Failed_list_Part_' + str(partx) + '.txt', 'w')
	for n in failed_ls:
		fa.write(str(n) + '\n')
	return
	
# RT_All_Gen1_12_Movie_Page_Sources_HTML
if not os.path.exists(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/'):
	os.makedirs(PATH + '/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/')
P1 = []
for i in range(1,26):
	p2 = Process(target = run4, args = (str(i),))
	P1.append(p2)
	p2.start()
for p in P1:
		p.join()
# p.close()

print(Fore.LIGHTGREEN_EX + 'Process finished')
exit()
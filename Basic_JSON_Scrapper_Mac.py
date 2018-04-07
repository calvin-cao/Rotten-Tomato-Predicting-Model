### Step 1: Below is the basic scrapper which can obtain and save all pages of the DVD-Streaming-All section from Rottentomatoes.com as one text file. ###
def run1(url,filename,pagenumber):
	import urllib.request, json
	import re
	import time
	import requests
	pageNum = int(pagenumber)
	fw = open('/Users/CalvinCao/Local/RT/RT_JSON_' + str(filename) + '.txt', 'w')
	for i in range(1, pageNum + 1):
		print('page', i)
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
		fw.write(str(data) + '\t' + 'Page' + str(i) + '\n')
		print('Done')
	fw.close()
	return

# Gen1_6
run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=1&certified&sortBy=release&type=dvd-streaming-all','Action',97)

run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=2&certified&sortBy=release&type=dvd-streaming-all','Animation',16)

run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=4&certified&sortBy=release&type=dvd-streaming-all','Art&Foreign',69)

run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=5&certified&sortBy=release&type=dvd-streaming-all','Classics',47)

run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=6&certified&sortBy=release&type=dvd-streaming-all','Comedy',156)

run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=8&certified&sortBy=release&type=dvd-streaming-all','Documentary',54)

# Gen7_12
run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=9&certified&sortBy=release&type=dvd-streaming-all','Drama',258)

run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=10&certified&sortBy=release&type=dvd-streaming-all','Horror',53)

run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=11&certified&sortBy=release&type=dvd-streaming-all','Kids&Family',31)

run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=13&certified&sortBy=release&type=dvd-streaming-all','Mystery',95)

run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=18&certified&sortBy=release&type=dvd-streaming-all','Romance',54)

run1('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=14&certified&sortBy=release&type=dvd-streaming-all','Scifi&Fantasy',50)

### Step 2: Get all urls from JSON files and store in a .txt file ###
def run2(filename):
	import re
	with open('/Users/CalvinCao/Local/RT/RT_JSON_' + str(filename) + '.txt', 'r') as myfile:
		data = myfile.read().replace('\n', '')
	# print(data)
	data_str = str(data)
	url_location = [m.start() for m in re.finditer("'url':", data_str)]
	# print(url_location)
	fw = open('/Users/CalvinCao/Local/RT/RT_URLs_' + str(filename) + '.txt', 'w')
	for x in url_location:
		url_start = x
		url_end = data_str.find(',', url_start)
		url = data_str[url_start + 8 : url_end - 1]
		movie_url = 'www.rottentomatoes.com' + url
		fw.write(str(movie_url) + '\n')
	fw.close()
	return

# Gen1_6
run2('Action')
run2('Animation')
run2('Art&Foreign')
run2('Classics')
run2('Comedy')
run2('Documentary')
# Gen7-12
run2('Drama')
run2('Horror')
run2('Kids&Family')
run2('Mystery')
run2('Romance')
run2('Scifi&Fantasy')

def run3():
	a = ['Action','Animation','Art&Foreign','Classics','Comedy','Documentary','Drama','Horror','Kids&Family','Mystery','Romance','Scifi&Fantasy']
	all_url_ls = []
	urls_ls = []
	for i in a:
		with open('/Users/CalvinCao/Local/RT/RT_URLs_' + str(i) + '.txt', 'r') as myfile:
			urls = myfile.read()
		urls_ls = urls.split('\n')
		for x in urls_ls:
			if not str(x) in all_url_ls:
				all_url_ls.append(str(x))
			else:
				continue
	r = 0
	for x in range(0,len(all_url_ls),600):
		r += 1
		fh = open('/Users/CalvinCao/Local/RT/RT_All_URLs_Gen1_12_Part_' + str(r) + '.txt','w')
		for s in all_url_ls[x : x + 600]:
			fh.write(str(s) + '\n')
		fh.close()
	return

### Step 3: Collect main pages for each movie on the URL list (.html) ###
def run4(partx):
	import os
	import time
	import requests
	from colorama import Fore, Back, Style
	with open('/Users/CalvinCao/Local/RT/RT_All_URLs_Gen1_12_Part_' + str(partx) + '.txt', 'r') as myfile:
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
				fh = open('/Users/CalvinCao/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html', 'w')
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
				if os.path.exists('/Users/CalvinCao/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html'):
					os.remove('/Users/CalvinCao/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html')
					time.sleep(1)
					continue
				else:
					time.sleep(1)
					continue
			print(Fore.LIGHTGREEN_EX + '  Done')
			print(Style.RESET_ALL)
			time.sleep(0.1)
			break
		if not os.path.exists('/Users/CalvinCao/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/' + x[25:] + '.html'):
			failed_ls.append(x)
			print(Fore.LIGHTRED_EX + 'FAILED: ' + x[25:])
			print(Style.RESET_ALL)
			continue
	fa = open('/Users/CalvinCao/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/Failed_list_Part_' + str(partx) + '.txt', 'w')
	for n in failed_ls:
		fa.write(str(n) + '\n')
	return

import multiprocessing

for i in range(1,26):
	p = multiprocessing.Process(target = run4, args = (str(i),))
	p.start()

"""
def run5():
	import os
	import time
	import requests
	from colorama import Fore, Back, Style
	with open('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_URLs.txt', 'r') as myfile:
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
				fh = open('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources_HTML/' + x[25:] + '.html', 'w')
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
				if os.path.exists('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources_HTML/' + x[25:] + '.html'):
					os.remove('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources_HTML/' + x[25:] + '.html')
					time.sleep(1)
					continue
				else:
					time.sleep(1)
					continue
			print(Fore.LIGHTGREEN_EX + '  Done')
			print(Style.RESET_ALL)
			time.sleep(0.1)
			break
		if not os.path.exists('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources_HTML/' + x[25:] + '.html'):
			failed_ls.append(x)
			print(Fore.LIGHTRED_EX + '  FAILED: ' + x[25:])
			print(Style.RESET_ALL)
			continue
	fa = open('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources_HTML/Failed_list.txt', 'w')
	for n in failed_ls:
		fa.write(str(n) + '\n')
	return

run5()
"""

# Get all HTML into one list as strings
import os
HTML_ALL_ls = []
HTML_ALL_ls_name = []
for x in os.listdir('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources/'):
	try:
		fh = open('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources/' + x, 'r')
		HTML_ALL_ls.append(fh.read())
		HTML_ALL_ls_name.append(x)
	except:
		print('Bad file: ' + x)
		continue
# print(HTML_ALL_ls_name)


def run6():
	import re
	a = -1
	for x in HTML_ALL_ls:
		a = a + 1
		print(str(a), [m.start() for m in re.finditer("meter-value", x)])
	return

run6()


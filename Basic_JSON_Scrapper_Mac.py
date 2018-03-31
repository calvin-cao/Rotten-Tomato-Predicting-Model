"""
def run2():
	import urllib.request
	import re
	import time
	import requests
	from colorama import Fore, Back, Style
	with open('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_URLs.txt', 'r') as myfile:
		urls = myfile.read()
	# print(urls[:300])
	urls_ls = urls.split('\n')
	# print(urls_ls[0])
	for x in urls_ls:
		print(x[25:])
		page = None
		for i in range(5):
			try:
				fw = open('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources/' + x[25:] + '.txt', 'w')
				page = urllib.request.urlopen('https://' + x)
				pagetext = page.read()
				fw.write(str(pagetext))
				fw.close()
				print(Fore.GREEN + 'Done')
				print(Style.RESET_ALL)
				break
			except Exception as e:
				print(Fore.YELLOW + 'Failed attept ' + str(i+1))
				print(Style.RESET_ALL)
				time.sleep(2)
		if not page:
			print(Fore.RED + 'FAILED: ' + x[25:])
			print(Style.RESET_ALL)
			continue
	return
"""

# Collect main pages for each movie on the URL list (.html)
"""
def run4():
	import time
	import requests
	from colorama import Fore, Back, Style
	with open('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_URLs.txt', 'r') as myfile:
		urls = myfile.read()
	urls_ls = urls.split('\n')
	for x in urls_ls:
		print(x[25:])
		for i in range(5):
			try:
				page = None
				pagetext = None
				fh = open('/Users/CalvinCao/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources_HTML/' + x[25:] + '.html', 'w')
				page = requests.get('https://' + x)
				pagetext = page.text
				fh.write(pagetext)
				fh.close()
				print(Fore.GREEN + 'Done')
				print(Style.RESET_ALL)
				break
			except:
				print(Fore.YELLOW + 'Failed attept: ' + str(i+1))
				print(Style.RESET_ALL)
				time.sleep(5)
		if not pagetext:
			print(Fore.RED + 'FAILED: ' + x[25:])
			print(Style.RESET_ALL)
			continue
	return

run4()
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


def run3():
	import re
	a = -1
	for x in HTML_ALL_ls:
		a = a + 1
		print(str(a), [m.start() for m in re.finditer("meter-value", x)])
	return

run3()


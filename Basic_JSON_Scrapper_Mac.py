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
				print(Fore.RED + 'Failed attept ' + str(i+1))
				print(Style.RESET_ALL)
				time.sleep(2)
		if not page:
			print(Fore.RED + 'FAILED ' + x[25:])
			print(Style.RESET_ALL)
			continue
	return


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
print(HTML_ALL_ls_name)


def run3():
	import re
	a = -1
	for x in HTML_ALL_ls:
		a = a + 1
		print(str(a), [m.start() for m in re.finditer("meter-value", x)])
	return
run3()


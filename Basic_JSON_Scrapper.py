'''
with urllib.request.urlopen("https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&certified&sortBy=release&type=dvd-streaming-all") as url:
    data = json.loads(url.read().decode())
    print(data)
'''

# Below is the basic scrapper which can obtain and save all pages of the DVD-Streaming-All section from Rottentomatoes.com as one text file.
def run(url):
    import urllib.request, json
    import re
    import time
    import requests
    pageNum = 467
    fw = open('C:/Local/RT/RT_DVD_Streaming_All_JSON.txt', 'w')
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

if __name__ == '__main__':
    url = 'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&certified&sortBy=release&type=dvd-streaming-all'
    run(url)


# Find all of the urls in data_str
# Attempt 2:
def run1():
    import re
    with open('C:/Local/RT/RT_DVD_Streaming_All_JSON.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')
    # print(data)
    data_str = str(data)
    url_location = [m.start() for m in re.finditer("'url':", data_str)]
    # print(url_location)
    fw = open('C:/Local/RT/RT_DVD_Streaming_All_URLs.txt', 'w')
    for x in url_location:
        url_start = x
        url_end = data_str.find(',', url_start)
        url = data_str[url_start + 8 : url_end - 1]
        movie_url = 'www.rottentomatoes.com' + url
        fw.write(str(movie_url) + '\n')
    fw.close()
    return

if __name__=='__main__':
    run1()

# Collect main pages for each movie on the URL list (.html)
def run4():
    import time
    import requests
    from colorama import Fore, Back, Style
    with open('C:/Local/RT/RT_DVD_Streaming_All_URLs.txt', 'r') as myfile:
        urls = myfile.read()
    urls_ls = urls.split('\n')
    for x in urls_ls:
        print(x[25:])
        page = None
        for i in range(5):
            try:
                fh = open('C:/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources_HTML/' + x[25:] + '.html', 'w')
                p = requests.get('https://' + x)
                fh.write(p.text)
                fh.close()
                print(Fore.GREEN + 'Done')
                print(Style.RESET_ALL)
                break
            except Exception as e:
                print(Fore.YELLOW + 'Failed attept: ' + str(i+1))
                print(Style.RESET_ALL)
                time.sleep(0.5)
        if not p:
            print(Fore.RED + 'FAILED: ' + x[25:])
            print(Style.RESET_ALL)
            continue
    return

run4()

# Collect main pages for each movie on the URL list (.txt)
def run2():
    import urllib.request
    import re
    import time
    import requests
    from colorama import Fore, Back, Style
    with open('C:/Local/RT/RT_DVD_Streaming_All_URLs.txt', 'r') as myfile:
        urls = myfile.read()
    # print(urls[:300])
    urls_ls = urls.split('\n')
    # print(urls_ls[0])
    for x in urls_ls:
        print(x[25:])
        page = None
        for i in range(5):
            try:
                fw = open('C:/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources_Text/' + x[25:] + '.txt', 'w')
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
                time.sleep(0.5)
        if not page:
            print(Fore.RED + 'FAILED: ' + x[25:])
            print(Style.RESET_ALL)
            continue
    return

run2()

# Loop through every file in one folder:
'''
import os
for x in os.listdir(os.getcwd()):
    # do your thing
    break
'''

# Get all HTML codes into one list as strings
import os
HTML_ALL_ls = []
HTML_ALL_ls_name = []
for x in os.listdir('C:/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources/'):
	try:
		fh = open('C:/Local/RT/RT_DVD_Streaming_All_Movie_Page_Sources/' + x, 'r')
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


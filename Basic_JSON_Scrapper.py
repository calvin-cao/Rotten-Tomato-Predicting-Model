'''
with urllib.request.urlopen("https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&certified&sortBy=release&type=dvd-streaming-all") as url:
    data = json.loads(url.read().decode())
    print(data)
'''

### Step 1: Below is the basic scrapper which can obtain and save all pages of the DVD-Streaming-All section from Rottentomatoes.com as one text file. ###
"""
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
"""

def run5(url,filename,pagenumber):
    import urllib.request, json
    import re
    import time
    import requests
    pageNum = int(pagenumber)
    fw = open('C:/Local/RT/RT_' + str(filename) + '_JSON.txt', 'w')
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
run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=1&certified&sortBy=release&type=dvd-streaming-all','Action',97)

run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=2&certified&sortBy=release&type=dvd-streaming-all','Animation',16)

run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=4&certified&sortBy=release&type=dvd-streaming-all','Art&Foreign',69)

run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=5&certified&sortBy=release&type=dvd-streaming-all','Classics',47)

run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=6&certified&sortBy=release&type=dvd-streaming-all','Comedy',156)

run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=8&certified&sortBy=release&type=dvd-streaming-all','Documentary',54)

# Gen7_12
run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=9&certified&sortBy=release&type=dvd-streaming-all','Drama',258)

run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=10&certified&sortBy=release&type=dvd-streaming-all','Horror',53)

run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=11&certified&sortBy=release&type=dvd-streaming-all','Kids&Family',31)

run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=13&certified&sortBy=release&type=dvd-streaming-all','Mystery',95)

run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=18&certified&sortBy=release&type=dvd-streaming-all','Romance',54)

run5('https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&genres=14&certified&sortBy=release&type=dvd-streaming-all','Scifi&Fantasy',50)


### Step 2: Get all urls from JSON files and store in a .txt file ###
"""
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
"""

# Attempt 3:
def run6(filename):
    import re
    with open('C:/Local/RT/RT_' + str(filename) + '_JSON.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')
    # print(data)
    data_str = str(data)
    url_location = [m.start() for m in re.finditer("'url':", data_str)]
    # print(url_location)
    fw = open('C:/Local/RT/RT_' + str(filename) + '_URLs.txt', 'w')
    for x in url_location:
        url_start = x
        url_end = data_str.find(',', url_start)
        url = data_str[url_start + 8 : url_end - 1]
        movie_url = 'www.rottentomatoes.com' + url
        fw.write(str(movie_url) + '\n')
    fw.close()
    return

# Gen1_6
run6('Action')
run6('Animation')
run6('Art&Foreign')
run6('Classics')
run6('Comedy')
run6('Documentary')
# Gen7-12
run6('Drama')
run6('Horror')
run6('Kids&Family')
run6('Mystery')
run6('Romance')
run6('Scifi&Fantasy')

def run7():
    a = ['Action','Animation','Art&Foreign','Classics','Comedy','Documentary','Drama','Horror','Kids&Family','Mystery','Romance','Scifi&Fantasy']
    all_url_ls = []
    urls_ls = []
    for i in a:
        with open('C:/Local/RT/RT_' + str(i) + '_URLs.txt', 'r') as myfile:
            urls = myfile.read()
        urls_ls = urls.split('\n')
        for x in urls_ls:
            if not str(x) in all_url_ls:
                all_url_ls.append(str(x))
            else:
                continue
    fh = open('C:/Local/RT/RT_Gen1_12_URLs.txt','w')
    for x in all_url_ls:
        fh.write(str(x) + '\n')
    fh.close()
    return

run7()


### Step 3: Collect main pages for each movie on the URL list (.html) ###
def run4(file):
    import os
    import time
    import requests
    from colorama import Fore, Back, Style
    with open('C:/Local/RT/RT_' + file + '_URLs.txt', 'r') as myfile:
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
                fh = open('C:/Local/RT/RT_' + file + '_Movie_Page_Sources_HTML/' + x[25:] + '.html', 'w')
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
                if os.path.exists('C:/Local/RT/RT_' + file + '_Movie_Page_Sources_HTML/' + x[25:] + '.html'):
                    os.remove('C:/Local/RT/RT_' + file + '_Movie_Page_Sources_HTML/' + x[25:] + '.html')
                    time.sleep(1)
                    continue
                else:
                    time.sleep(1)
                    continue
            print(Fore.LIGHTGREEN_EX + '  Done')
            print(Style.RESET_ALL)
            time.sleep(0.1)
            break
        if not os.path.exists('C:/Local/RT/RT_' + file + '_Movie_Page_Sources_HTML/' + x[25:] + '.html'):
            failed_ls.append(x)
            print(Fore.LIGHTRED_EX + 'FAILED: ' + x[25:])
            print(Style.RESET_ALL)
            continue
    fa = open('C:/Local/RT/RT_' + file + '_Movie_Page_Sources_HTML/Failed_list.txt', 'w')
    for n in failed_ls:
        fa.write(str(n) + '\n')
    return

run4('Gen1_12')

# Collect main pages for each movie on the URL list (.txt)
"""
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
"""

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


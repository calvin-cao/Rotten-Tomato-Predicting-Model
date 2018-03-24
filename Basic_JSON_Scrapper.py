import urllib.request, json
import re
import time
import requests

'''
with urllib.request.urlopen("https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&certified&sortBy=release&type=dvd-streaming-all") as url:
    data = json.loads(url.read().decode())
    print(data)
'''

def run(url):
    pageNum=467
    fw=open('C:/Users/calvi/Dropbox/Desktop/RT_DVD_Streaming_All_JSON.txt','w')
    for i in range(1,pageNum+1):
        print('page',i)
        if i==1:
            pageLink=url
        else:
            pageLink=url+'&page='+str(i)
        for ii in range(5):
            try:
                with urllib.request.urlopen(pageLink) as url1:
                    data=json.loads(url1.read().decode())
            except Exception as e:
                print('failed attept',ii)
                time.sleep(2)
        fw.write(str(data)+'\t'+'Page'+str(i)+'\n')
        print('Done')
    fw.close()

if __name__=='__main__':
    url='https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&certified&sortBy=release&type=dvd-streaming-all'
    run(url)

# This basic scrapper can obtain and save all pages of the DVD-Streaming-All section from Rottentomatoes.com as one text file.
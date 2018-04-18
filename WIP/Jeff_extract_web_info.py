### Jeff's Parser ###
# pageLink = 'https://www.rottentomatoes.com/m/2012'
# pageLink = 'https://www.rottentomatoes.com/m/thelma_2017'
pageLink = 'https://www.rottentomatoes.com/m/black_panther_2018'

from bs4 import BeautifulSoup
import requests, re

#parse the whole html
response = requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
html = response.content # get the html
soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 

#get 'TOMATOMETER'
Critics_Score = int(soup.find('span',{'class':'meter-value superPageFontColor'}).text[:-1])

#get 'AUDIENCE SCORE'
Audience_Score = int(soup.find('span',{'style':'vertical-align:top'}).text[:-1])

#estimate 'TOMATOMETER' by sample mean from 'CRITICS REVIEWS'
rotten = soup.findAll('span', {'class':re.compile('small rotten')})
fresh = soup.findAll('span', {'class':re.compile('small fresh')})
Critics_Sample_Score = len(fresh)/(len(fresh)+len(rotten))*100


#get 'Critic Consensus'
Critic_Consensus = soup.find('p',{'class':'critic_consensus superPageFontColor'}).text.split('\n')[2].strip()

#get 'MOVIE INFO'
Summary = soup.find('div',{'id':'movieSynopsis'}).text.split('\n')[1].strip()

#get all content as a string
Content = ''
for c in soup.findAll('div',{'class':re.compile('meta-value')}):
    Content += (c.text.strip() + ' ')

#get content by each class
for i in range(len(soup.findAll('div',{'class':re.compile('meta-label subtle')}))):   
    exec(soup.findAll('div',{'class':re.compile('meta-label subtle')})[i].text.strip()[:-1].replace(' ','_').replace('/','_') + " = soup.findAll('div',{'class':re.compile('meta-value')})[i].text.strip()")

#get CAST as a string
castSection = soup.find('div',{'class':'castSection'})
Cast = ''
for c in castSection.findAll('a',{'href':re.compile('/celebrity/')}):
    if c.text != '\n': Cast += c.text.strip() + ','
Cast = Cast.replace(' ', '') #combine each name

'''#same result but slow
Cast = ''
for i in range(1, len(castSection.findAll('a',{'href':re.compile('/celebrity/')})), 2):
    Cast += (castSection.findAll('a',{'href':re.compile('/celebrity/')})[i].text.strip() + ',')
'''

#get all 'CRITICS REVIEWS' as a string
CriticSection = soup.find('div',{'id':'reviews'})
Critic_Reviews = ''
for i in range(0, len(CriticSection.findAll('div',{'class':re.compile('media-body')})), 2):
    Critic_Reviews += (CriticSection.findAll('div',{'class':re.compile('media-body')})[i].text.split('\n\n')[1].strip() + ' ')

#get all 'AUDIENCE REVIEWS' as a string
Audience_Reviews = ''
for c in soup.findAll('p',{'class':re.compile('comment clamp clamp-6')}):
    Audience_Reviews += (c.text.strip() + ' ')


#modify variables in Content
try: Rating = Rating.replace(' ', '') #combine words
except Exception: pass
try: Genre = Genre.replace(' ', '').replace('\n', '') #combine words
except Exception: pass
try: Directed_By = Directed_By.replace(' ', '') #combine words
except Exception: pass
try: Written_By = Written_By.replace(' ', '') #combine words
except Exception: pass
try: Studio = Studio.replace(' ', '') #combine words
except Exception: pass

try: In_Theaters_month = In_Theaters[:3] #extract In Theaters month
except Exception: pass
try: In_Theaters_year = int(In_Theaters.split(', ')[1][:4]) #extract In Theaters year
except Exception: pass
try: On_Disc_Streaming_month = On_Disc_Streaming[:3] #extract On Disc month
except Exception: pass
try: On_Disc_Streaming_year = int(On_Disc_Streaming.split(', ')[1][:4]) #extract On Disc year
except Exception: pass

try: Box_Office = int(Box_Office[1:].replace(',',''))
except Exception: pass
try: Runtime = int(Runtime[:-8])
except Exception: pass


# Now what we got

Critics_Score
Audience_Score
Critics_Sample_Score

Critic_Consensus
Summary
Critic_Reviews
Audience_Reviews
Cast

Content
#in Content
Rating
Genre
Directed_By
Written_By
Studio
In_Theaters_month
On_Disc_Streaming_month

In_Theaters_year
On_Disc_Streaming_year
Box_Office
Runtime
"""

write:Critics_Score + '/t' + Audience_Score + '/t' +
+ '/n'
"""

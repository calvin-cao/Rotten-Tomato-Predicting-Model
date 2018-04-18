from bs4 import BeautifulSoup
import re
import os

a = os.listdir("C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/")
b = []
for x in a:
    x = "C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/" + x
    if not '.txt' in x:
        b.append(x)
# print(b[0])
# print(len(b))

CS = [] # Critics_Score
AS = [] # Audience_Score
CC = [] # Critic Consensus
MI = [] # Summary
CT = [] # Content
CA = [] # Cast
CR = [] # Critics_Reviews
AR = [] # Audience_Reviews

f = open('a.txt', 'w')
# soup = BeautifulSoup(open(b[0]), 'lxml')
i = 0
for x in b:
    soup = BeautifulSoup(open(x),'lxml')
    i += 1
    try:
        CS.append(int(soup.find('span',{'class':'meter-value superPageFontColor'}).text[:-1]))
        AS.append(int(soup.find('span',{'style':'vertical-align:top'}).text[:-1]))
        print(str(i), 'Success')
    except:
        CS.append(None)
        print(str(i), 'Failed')
        continue
    """
    AS.append(int(soup.find('span',{'style':'vertical-align:top'}).text[:-1]))
    CC.append(soup.find('p',{'class':'critic_consensus superPageFontColor'}).text.split('\n')[2].strip())
    MI.append(soup.find('div',{'id':'movieSynopsis'}).text.split('\n')[1].strip())
    Content = ''
    for c in soup.findAll('div',{'class':re.compile('meta-value')}):
        Content += (c.text.strip() + ' ')
    CT.append(Content)
    castSection = soup.find('div',{'class':'castSection'})
    Cast = ''
    for c in castSection.findAll('a',{'href':re.compile('/celebrity/')}):
        if c.text != '\n':
            Cast += c.text.strip() + ','
    Cast = Cast.replace(' ', '')
    CA.append(Cast)
    CriticSection = soup.find('div',{'id':'reviews'})
    Critic_Reviews = ''
    for i in range(0, len(CriticSection.findAll('div',{'class':re.compile('media-body')})), 2):
        Critic_Reviews += (CriticSection.findAll('div',{'class':re.compile('media-body')})[i].text.split('\n\n')[1].strip() + ' ')
    CR.append(Critic_Reviews)
    Audience_Reviews = ''
    for c in soup.findAll('p',{'class':re.compile('comment clamp clamp-6')}):
        Audience_Reviews += (c.text.strip() + ' ')
    AR.append(Audience_Reviews)
    """
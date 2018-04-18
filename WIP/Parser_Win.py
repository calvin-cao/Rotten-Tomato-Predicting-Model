from bs4 import BeautifulSoup
import re
import os
import time

a = os.listdir("C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/")
b = []
for x in a[:100]:
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

# f = open('a.txt', 'w')
# soup = BeautifulSoup(open(b[0]), 'lxml')
start_time = time.clock()
i = 0
for x in b:
    soup = BeautifulSoup(open(x),'lxml')
    i += 1

    try:
        CS.append(int(soup.find('span',{'class':'meter-value superPageFontColor'}).text[:-1]))
    except:
        CS.append(None)
        print(str(i), 'CS Failed')
        #continue
    
    try:
        AS.append(int(soup.find('span',{'style':'vertical-align:top'}).text[:-1]))
    except:
        AS.append(None)
        print(str(i), 'AS Failed')
        #continue
    
    try:
        CC.append(soup.find('p',{'class':'critic_consensus superPageFontColor'}).text.split('\n')[2].strip())
    except:
        CC.append(None)
        print(str(i), 'CC Failed')
        #continue

    # a = int(soup.find('span',{'class':'subtle superPageFontColor'}).text[:-1])
    
    
    try:
        MI.append(soup.find('div',{'id':'movieSynopsis'}).text.split('\n')[1].strip())
    except:
        MI.append(None)
        print(str(i), 'MI Failed')
        #continue
    
    try:
        Content = ''
        for c in soup.findAll('div',{'class':re.compile('meta-value')}):
            Content += (c.text.strip() + ' ')
        CT.append(Content)
    except:
        CT.append(None)
        print(str(i), 'CT Failed')
        #continue
    
    try:
        castSection = soup.find('div',{'class':'castSection'})
        Cast = ''
        for c in castSection.findAll('a',{'href':re.compile('/celebrity/')}):
            if c.text != '\n':
                Cast += c.text.strip() + ','
        Cast = Cast.replace(' ', '')
        CA.append(Cast)
    except:
        CA.append(None)
        print(str(i), 'CA Failed')
        #continue
    
    try:
        CriticSection = soup.find('div',{'id':'reviews'})
        Critic_Reviews = ''
        for i in range(0, len(CriticSection.findAll('div',{'class':re.compile('media-body')})), 2):
            Critic_Reviews += (CriticSection.findAll('div',{'class':re.compile('media-body')})[i].text.split('\n\n')[1].strip() + ' ')
        CR.append(Critic_Reviews)
    except:
        CR.append()
        print(str(i), 'CR Failed')
        #continue
    
    try:
        Audience_Reviews = ''
        for c in soup.findAll('p',{'class':re.compile('comment clamp clamp-6')}):
            Audience_Reviews += (c.text.strip() + ' ')
        AR.append(Audience_Reviews)
    except:
        AR.append(None)
        print(str(i), 'AR Failed')
        #continue

fh = open("C:/Local/RT/test.txt", 'w', encoding = 'utf-8')
for x in range(len(b)):
    fh.write(a[x][:a[x].find('.html')] + '\t' + str(CS[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(AS[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(CC[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(MI[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(CT[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(CA[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(CR[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(AR[x]).replace('\n', " ").replace('\t', ' ') + '\n' + '\n' + '\n')
fh.close()
print("--- %s seconds ---" % (time.clock() - start_time))
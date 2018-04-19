from bs4 import BeautifulSoup
import re
import os
import time
a = os.listdir("C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/")
b = []
for x in a[:20]:
    x = "C:/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/" + x
    if not '.txt' in x:
        b.append(x)
CS = [] # Critics_Score
AS = [] # Audience_Score
CC = [] # Critic Consensus
RA = [] # Rating
GE = [] # Genre
DB = [] # Directed_By
WB = [] # Written_By
ST = [] # Studio
ITD = [] # In_Theaters_date
ODSD = [] # On_Disc_Streaming_date
BO = [] # Box_Office
RU = [] # Runtime
MI = [] # Summary
# CT = [] # Content
CA = [] # Cast
CR = [] # Critics_Reviews
AR = [] # Audience_Reviews
start_time = time.clock()
asdaf = 0
for x in b:
    soup = BeautifulSoup(open(x),'lxml')
    asdaf += 1
    print(asdaf)
    try:
        CS.append(int(soup.find('span',{'class':'meter-value superPageFontColor'}).text[:-1]))
    except:
        CS.append(None)
        print('CS Failed')
        #continue
    try:
        AS.append(int(soup.find('span',{'style':'vertical-align:top'}).text[:-1]))
    except:
        AS.append(None)
        print('AS Failed')
        #continue
    try:
        CC.append(soup.find('p',{'class':'critic_consensus superPageFontColor'}).text.split('\n')[2].strip())
    except:
        CC.append(None)
        print('CC Failed')
        #continue
    # a = int(soup.find('span',{'class':'subtle superPageFontColor'}).text[:-1])
    try:
        MI.append(soup.find('div',{'id':'movieSynopsis'}).text.split('\n')[1].strip())
    except:
        MI.append(None)
        print('MI Failed')
        #continue
    Content = ''
    for c in soup.findAll('div',{'class':re.compile('meta-value')}):
        Content += (c.text.strip() + ' ')
    for i in range(len(soup.findAll('div',{'class':re.compile('meta-label subtle')}))):   
        exec(soup.findAll('div',{'class':re.compile('meta-label subtle')})[i].text.strip()[:-1].replace(' ','_').replace('/','_') + " = soup.findAll('div',{'class':re.compile('meta-value')})[i].text.strip()")
    try:
        RA.append(Rating.replace(' ', '')) #combine words
    except Exception:
        RA.append(None)
        print('RA Failed')
    try:
        GE.append(Genre.replace(' ', '').replace('\n', '')) #combine words
    except Exception:
        GE.append(None)
        print('GE Failed')
    try:
        DB.append(Directed_By.replace(' ', '')) #combine words
    except Exception:
        DB.append(None)
        print('DB Failed')
    try:
        WB.append(Written_By.replace(' ', '')) #combine words
    except Exception:
        WB.append(None)
        print('WB Failed')
    try:
        ST.append(Studio.replace(' ', '')) #combine words
    except Exception:
        ST.append(None)
        print('ST Failed')
    try:
        ITD.append(In_Theaters) #extract In Theaters month
    except Exception:
        ITD.append(None)
        print('ITD Failed')
    try:
        ODSD.append(On_Disc_Streaming) #extract On Disc month
    except Exception:
        ODSD.append(None)
        print('ODSD Failed')
    try:
        BO.append(int(Box_Office[1:].replace(',','')))
    except Exception:
        BO.append(None)
        print('BO Failed')
    try:
        RU.append(int(Runtime[:-8]))
    except Exception:
        RU.append(None)
        print('RU Failed')
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
        print('CA Failed')
        #continue
    try:
        CriticSection = soup.find('div',{'id':'reviews'})
        Critic_Reviews = ''
        for i in range(0, len(CriticSection.findAll('div',{'class':re.compile('media-body')})), 2):
            Critic_Reviews += (CriticSection.findAll('div',{'class':re.compile('media-body')})[i].text.split('\n\n')[1].strip() + ' ')
        CR.append(Critic_Reviews)
    except:
        CR.append(None)
        print('CR Failed')
        #continue
    try:
        Audience_Reviews = ''
        for c in soup.findAll('p',{'class':re.compile('comment clamp clamp-6')}):
            Audience_Reviews += (c.text.strip() + ' ')
        AR.append(Audience_Reviews)
    except:
        AR.append(None)
        print('AR Failed')
        #continue
fh = open("C:/Local/RT/test.txt", 'w', encoding = 'utf-8')
fh.write('Movie_name' + '\t' + 'Critics_Score' + '\t' + 'Audience_Score' + '\t' + 'Critic Consensus' + '\t' + 'Rating' + '\t' + 'Genre' + '\t' + 'Directed_By' + '\t' + 'Written_By' + '\t' + 'Studio' + '\t' + 'In_Theaters_date' + '\t' + 'On_Disc_Streaming_date' + '\t' + 'Box_Office' + '\t' + 'Runtime' + '\t' + 'Summary' + '\t' + 'Cast' + '\t' + 'Critics_Reviews' + '\t' + 'Audience_Reviews' + '\n')
for x in range(len(b)):
    fh.write(a[x] + '\t' + str(CS[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(AS[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(RA[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(GE[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(DB[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(WB[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(ST[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(ITD[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(ODSD[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(BO[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(RU[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(MI[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(CA[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(CR[x]).replace('\n', " ").replace('\t', ' ') + '\t' + str(AR[x]).replace('\n', " ").replace('\t', ' ') + '\n' + '\n' + '\n')
fh.close()
print("--- %s seconds ---" % (time.clock() - start_time))

"""
CS = [] # Critics_Score
AS = [] # Audience_Score
CC = [] # Critic Consensus
RA = [] # Rating
GE = [] # Genre
DB = [] # Directed_By
WB = [] # Written_By
ST = [] # Studio
ITD = [] # In_Theaters_date
ODSD = [] # On_Disc_Streaming_date
BO = [] # Box_Office
RU = [] # Runtime
MI = [] # Summary
# CT = [] # Content
CA = [] # Cast
CR = [] # Critics_Reviews
AR = [] # Audience_Reviews

len(CS)
len(AS)
len(RA)
len(GE)
len(DB)
len(WB)
len(ST)
len(ITD)
len(ODSD)
len(BO)
len(RU)
len(MI)
len(CA)
len(CR)
len(AR)
"""
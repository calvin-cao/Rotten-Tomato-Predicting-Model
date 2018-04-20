import os
import time
from multiprocessing import Process, Manager

PATH = input("Please enter html files' path: ")
if len(PATH) < 1:
	PATH = "/Users/CalvinCao/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/"
start_time = time.clock()
A = [PATH + x for x in os.listdir(PATH) if x.endswith('.html')]
B = {}
i = 0
for x in range(0,len(A),200):
	i += 1
	B[str(i)] = []
	for s in A[x : x + 200]:
		B[str(i)].append(s)
del(i,A)

"""
for x in B.values():
	print(len(x))
"""

def run():
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
		try:
			g = open(x)
			html = g.read().encode('utf-8')
			selector = etree.HTML(html)
			tomatometers= selector.xpath('//*[@id="scoreStats"]/div[2]')
			for tomatometer in tomatometers:
				reviews_counted=tomatometer.xpath('//*[@id="scoreStats"]/div[2]/span[2]')
			RC.append(reviews_counted[0].text)
		except:
			RC.append(None)
			print('RC Failed')
		try:
			audiences=selector.xpath('//*[@id="scorePanel"]/div[2]/div[2]')
			for audience in audiences:
				users_rating_text=audience.xpath('//*[@id="scorePanel"]/div[2]/div[2]/div[2]/text()')
				users_rating=users_rating_text[1].split()[0]
			UR.append(users_rating)
		except:
			UR.append(None)
			print('UR Failed')
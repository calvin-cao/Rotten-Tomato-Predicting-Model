import re
import os
import time
from bs4 import BeautifulSoup
from lxml import etree
from multiprocessing import Process, Manager


PATH = input("Please enter html files' path: \n")
if len(PATH) < 1:
	PATH = "/Users/CalvinCao/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/"
MNG = Manager()
start_time = time.time()

def run(List,PartN):
	asdaf = 0
	for x in List:
		soup = BeautifulSoup(open(x),'lxml')
		asdaf += 1
		print(str(PartN) + '.' + str(asdaf))
		try:
			CS = int(soup.find('span',{'class':'meter-value superPageFontColor'}).text[:-1])
		except:
			CS = None
			print('CS Failed')
			#continue
		try:
			AS = int(soup.find('span',{'style':'vertical-align:top'}).text[:-1])
		except:
			AS = None
			print('AS Failed')
			#continue
		try:
			CC = soup.find('p',{'class':'critic_consensus superPageFontColor'}).text.split('\n')[2].strip()
		except:
			CC = None
			print('CC Failed')
			#continue
		# a = int(soup.find('span',{'class':'subtle superPageFontColor'}).text[:-1])
		try:
			MI = soup.find('div',{'id':'movieSynopsis'}).text.split('\n')[1].strip()
		except:
			MI = None
			print('MI Failed')
			#continue
		try:
			ARS = {}
			for i in range(len(soup.findAll('div',{'class':re.compile('meta-label subtle')}))):
				ARS[str(soup.findAll('div',{'class':re.compile('meta-label subtle')})[i].text.strip()[:-1].replace(' ','_').replace('/','_'))] = soup.findAll('div',{'class':re.compile('meta-value')})[i].text.strip()
			try:
				RA = str(ARS['Rating'])
			except:
				RA = None
				print('RA failed')
			try:
				GE = str(ARS['Genre']).replace(' ', '').replace('\n', '')
			except:
				GE = None
				print('GE failed')
			try:
				DB = str(ARS['Directed_By'])
			except:
				DB = None
				print('DB failed')
			try:
				WB = str(ARS['Written_By'])
			except:
				WB = None
				print('WB failed')
			try:
				ST = str(ARS['Studio'])
			except:
				ST = None
				print('ST failed')
			try:
				ITD = str(ARS['In_Theaters'])[:str(ARS['In_Theaters']).find('\n')]
			except:
				ITD = None
				print('ITD failed')
			try:
				ODSD = str(ARS['On_Disc_Streaming'])
			except:
				ODSD = None
				print('ODSD failed')
			try:
				BO = str(ARS['Box_Office'])
			except:
				BO = None
				print('BO failed')
			try:
				RU = str(ARS['Runtime'])
			except:
				RU = None
				print('RU failed')
		except:
			print('CT failed')
		try:
			castSection = soup.find('div',{'class':'castSection'})
			Cast = ''
			for c in castSection.findAll('a',{'href':re.compile('/celebrity/')}):
				if c.text != '\n':
					Cast += c.text.strip() + ','
			Cast = Cast.replace(' ', '')
			CA = Cast
		except:
			CA = None
			print('CA Failed')
			#continue
		try:
			CriticSection = soup.find('div',{'id':'reviews'})
			Critic_Reviews = ''
			for i in range(0, len(CriticSection.findAll('div',{'class':re.compile('media-body')})), 2):
				Critic_Reviews += (CriticSection.findAll('div',{'class':re.compile('media-body')})[i].text.split('\n\n')[1].strip() + ' ')
			CR = Critic_Reviews
		except:
			CR = None
			print('CR Failed')
			#continue
		try:
			Audience_Reviews = ''
			for c in soup.findAll('p',{'class':re.compile('comment clamp clamp-6')}):
				Audience_Reviews += (c.text.strip() + ' ')
			AR = Audience_Reviews
		except:
			AR = None
			print('AR Failed')
			#continue
		try:
			g = open(x)
			html = g.read().encode('utf-8')
			selector = etree.HTML(html)
			tomatometers= selector.xpath('//*[@id="scoreStats"]/div[2]')
			for tomatometer in tomatometers:
				reviews_counted=tomatometer.xpath('//*[@id="scoreStats"]/div[2]/span[2]')
			RC = reviews_counted[0].text
		except:
			RC = None
			print('RC Failed')
		try:
			audiences=selector.xpath('//*[@id="scorePanel"]/div[2]/div[2]')
			for audience in audiences:
				users_rating_text=audience.xpath('//*[@id="scorePanel"]/div[2]/div[2]/div[2]/text()')
				users_rating=users_rating_text[1].split()[0]
			UR = users_rating
		except:
			UR = None
			print('UR Failed')
		AIA.append(str(List[asdaf - 1])[str(List[asdaf - 1]).find('HTML/') + 5:str(List[asdaf - 1]).find('.html')] + '\t' + str(CS).replace('\n', " ").replace('\t', ' ') + '\t' + str(AS).replace('\n', " ").replace('\t', ' ') + '\t' + str(CC).replace('\n', " ").replace('\t', ' ') + '\t' + str(RA).replace('\n', " ").replace('\t', ' ') + '\t' + str(GE).replace('\n', " ").replace('\t', ' ') + '\t' + str(DB).replace('\n', " ").replace('\t', ' ') + '\t' + str(WB).replace('\n', " ").replace('\t', ' ') + '\t' + str(ST).replace('\n', " ").replace('\t', ' ') + '\t' + str(ITD).replace('\n', " ").replace('\t', ' ') + '\t' + str(ODSD).replace('\n', " ").replace('\t', ' ') + '\t' + str(BO).replace('\n', " ").replace('\t', ' ') + '\t' + str(RU).replace('\n', " ").replace('\t', ' ') + '\t' + str(MI).replace('\n', " ").replace('\t', ' ') + '\t' + str(CA).replace('\n', " ").replace('\t', ' ') + '\t' + str(CR).replace('\n', " ").replace('\t', ' ') + '\t' + str(AR).replace('\n', " ").replace('\t', ' ') + '\t' + str(RC).replace('\n', " ").replace('\t', ' ') + '\t' + str(UR).replace('\n', " ").replace('\t', ' ') + '\n')

A = [PATH + x for x in os.listdir(PATH) if x.endswith('.html')]
B = {}
i = 0
for x in range(0,len(A),3800):
	i += 1
	B[str(i)] = []
	for s in A[x : x + 3800]:
		B[str(i)].append(s)
del(i,A)

AIA = MNG.list()
Processes = []
for i in range(4):
	p = Process(target = run, args = (B[str(i+1)],i+1))
	Processes.append(p)
	p.start()
for p in Processes:
	p.join()

fh = open(PATH + 'test.txt', 'w')
fh.write('Movie_name' + '\t' + 'Critics_Score' + '\t' + 'Audience_Score' + '\t' + 'Critic_Consensus' + '\t' + 'Rating' + '\t' + 'Genre' + '\t' + 'Directed_By' + '\t' + 'Written_By' + '\t' + 'Studio' + '\t' + 'In_Theaters_date' + '\t' + 'On_Disc_Streaming_date' + '\t' + 'Box_Office' + '\t' + 'Runtime' + '\t' + 'Summary' + '\t' + 'Cast' + '\t' + 'Critics_Reviews' + '\t' + 'Audience_Reviews' + '\t' + 'Critics_Reviewer_Count' + '\t' + 'Audience_Reviewer_Count' + '\n')
for x in AIA:
	fh.write(x)
fh.close()
print("--- %s seconds ---" % (time.time() - start_time))


from bs4 import BeautifulSoup
import re
import os
import time
from lxml import etree
from time import gmtime, strftime
PATH = input("Please enter html files' path:")
if len(PATH) < 1:
    PATH = "S:/Analytics Clients/Fandango Research/RottenTomatoes work/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/"
start_time = time.clock()


def getMovieInfo(List):
	for x in List:
		soup = BeautifulSoup(open(x),'lxml')
		l.write(x.replace(PATH, '').replace('.html', '') + '-')
		
		try:    #Tomatometer
			CS = soup.find('span',{'class':'meter-value superPageFontColor'}).text
		except:
			CS = None
			l.write('Tomatometer Failed, ')
			
		try:	#Audience Score
			AS = soup.find('span',{'style':'vertical-align:top'}).text
		except:
			AS = None
			l.write('Audience Score Failed, ')
			
		try:	#Critics Consensus
			CC = soup.find('p',{'class':'critic_consensus superPageFontColor'}).text.split('\n')[2].strip()
		except:
			CC = None
			l.write('Critic Consensus Failed, ')
			
		try:	#Movie Summary
			MI = soup.find('div',{'id':'movieSynopsis'}).text.split('\n')[1].strip()
		except:
			MI = None
			l.write('Movie Summary Failed, ')
			
		try:	#Movie Details
			MD = {}
			for i in range(len(soup.findAll('div',{'class':re.compile('meta-label subtle')}))):
				MD[str(soup.findAll('div',{'class':re.compile('meta-label subtle')})[i].text.strip()[:-1].replace(' ','_').replace('/','_'))] = soup.findAll('div',{'class':re.compile('meta-value')})[i].text.strip()
				
			try:	#Rating
				RA = str(MD['Rating'])
			except:
				RA = None
				l.write('Rating Failed, ')
				
			try:	#Genre
				GE = re.sub('\s+', ' ', str(MD['Genre']).replace('\n', ''))
			except:
				GE = None
				l.write('Genre Failed, ')
				
			try:	#Director
				DB = str(MD['Directed_By'])
			except:
				DB = None
				l.write('Director Failed, ')
				
			try:	#Writer
				WB = str(MD['Written_By'])
			except:
				WB = None
				l.write('Writer Failed, ')
				
			try:	#Studio
				ST = str(MD['Studio'])
			except:
				ST = None
				l.write('Studio Failed, ')
				
			try:	#In Theatres Release Date
				ITD = str(MD['In_Theaters'])
			except:
				ITD = None
				l.write('In Theatres Date Failed, ')
				
			try:	#On Disc Streaming Date
				ODSD = str(MD['On_Disc_Streaming'])
			except:
				ODSD = None
				l.write('ODSD Failed, ')
				
			try:	#Box Office
				BO = str(MD['Box_Office'])
			except:
				BO = None
				l.write('Box Office Failed, ')
				
			try:	#Runtime
				RU = str(MD['Runtime'])
			except:
				RU = None
				l.write('Runtime Failed, ')
				
		except:
			l.write('Movie Details Failed, ')
			
		try:	#Cast
			castSection = soup.find('div',{'class':'castSection'})
			Cast = ''
			for c in castSection.findAll('a',{'href':re.compile('/celebrity/')}):
				if c.text != '\n':
					Cast += c.text.strip().replace(',','.') + ','
			# Cast = Cast.replace(' ', '')
			CA = Cast[:-1]
		except:
			CA = None
			l.write('Cast Failed, ')
			
		try:	#Critics Review
			CriticSection = soup.find('div',{'id':'reviews'})
			Critic_Reviews = ''
			for i in range(0, len(CriticSection.findAll('div',{'class':re.compile('media-body')})), 2):
				Critic_Reviews += (CriticSection.findAll('div',{'class':re.compile('media-body')})[i].text.split('\n\n')[1].strip() + '-x-')
			CR = Critic_Reviews
		except:
			CR = None
			l.write('Critics Reviews Failed, ')
			
		try:	#Audience Reviews
			Audience_Reviews = ''
			for c in soup.findAll('p',{'class':re.compile('comment clamp clamp-6')}):
				Audience_Reviews += (c.text.strip() + '-x-')
			AR = Audience_Reviews
		except:
			AR = None
			l.write('Audience Reviews Failed, ')
			
		try:	#Critics Reviews Counted
			g = open(x)
			html = g.read().encode('utf-8')
			selector = etree.HTML(html)
			tomatometers= selector.xpath('//*[@id="scoreStats"]/div[2]')
			for tomatometer in tomatometers:
				reviews_counted=tomatometer.xpath('//*[@id="scoreStats"]/div[2]/span[2]')
			RC = reviews_counted[0].text
		except:
			RC = None
			l.write('Reviews Counted Failed, ')
			
		try:	#User Rating
			audiences=selector.xpath('//*[@id="scorePanel"]/div[2]/div[2]')
			for audience in audiences:
				users_rating_text=audience.xpath('//*[@id="scorePanel"]/div[2]/div[2]/div[2]/text()')
			users_rating=users_rating_text[1].split()[0]
			UR = users_rating
		except:
			UR = None
			l.write('User Rating Failed, ')
		  
		try:	#Critics Avg Rating
			car = selector.xpath('//*[@id="scoreStats"]/div[1]')
			for cars in car:
				cavgrating = cars.xpath('//*[@id="scoreStats"]/div[1]/text()')
			cavgr = cavgrating[1].split()[0]
		except:
			cavgr = None
			l.write('Critics Avg Rating Failed, ')

		try:	#User Avg Rating
			uar = selector.xpath('//*[@id="scorePanel"]/div[2]/div[2]/div[1]')
			for uars in uar:
				uavgrating = uars.xpath('//*[@id="scorePanel"]/div[2]/div[2]/div[1]/text()')
			uavgr = uavgrating[1].split()[0]
		except:
			uavgr = None
			l.write('User Avg Rating Failed, ')

		try:	#Movie Name
			if soup.find('div', {'class':'heroImage movie'}):
				MovieName = soup.find('h1',{'data-type':'title'}).text.strip()
			elif soup.find('div', {'class':'heroImage movie noCursor'}):
				MovieName = soup.find('h1',{'data-type':'title'}).text.strip()[:-4]
			else:
				MovieName = soup.find('h1',{'data-type':'title'}).text.strip()[:-7]
		except:
			MovieName = ''
			l.write('Movie Name Failed, ')
			
		try:	#Franchise
			if soup.find('div', {'class':'franchiseLink'}):
				FR = soup.find('div', {'class':'franchiseLink'}).text.strip().replace('View Collection\n\n\n\nView the Collection:\n\n\nPart of the Collection:\n\n\n                                ', '')
			else:
				FR = 'No Franchisee'
		except:
			FR = None
			
			
		AIA.append(x.replace(PATH, '').replace('.html', '') + '|' + str(MovieName).replace('|', '-') + '|' + str(AS).replace('\n', '').replace('\t', '') + '|' + str(CS).replace('\n', '').replace('\t', '') + '|' + str(CA).replace('\n', " ").replace('\t', ' ') + '|' + str(MI).replace('\n', " ").replace('\t', ' ').replace('|', '-') + '|' + str(ITD).replace('\n\xa0', ' ').replace('\t', '') + '|' + str(ODSD).replace('\t', '') + '|' + str(GE).replace('\n', "").replace('\t', '').replace('|', '-') + '|' + str(ST).replace('\n', " ").replace('\t', ' ') + '|' + str(DB).replace('\n', " ").replace('\t', ' ') + '|' + str(RU).replace('\n', '').replace('\t', ' ') + '|' + str(BO).replace('\n', '').replace('\t', '') + '|' + str(RA).replace('\n', '').replace('\t', ' ').replace('|', '-') + '|' + str(WB).replace('\n', '').replace('\t', ' ') + '|' + str(cavgr).replace('\n', '').replace('\t', '') + '|' + str(uavgr).replace('\n', '').replace('\t', '') + '|' + str(RC).replace('\n', '').replace('\t', '') + '|' + str(UR).replace('\n', '').replace('\t', '') + '|' + str(FR).replace('\n', '').replace('\t', '').replace('|', '-') + '|' + str(CR).replace('\n', '').replace('\t', '').replace('|', '-') + '|' + str(AR).replace('\n', '').replace('\t', '').replace('|', '-') + '|' + str(CC).replace('\n', ' ').replace('\t', ' ').replace('|', '-') + '\n')
		l.write(' Done \n')

		
		
AIA = []
l = open(PATH + 'log_getMovieInfo.txt', 'a')


getMovieInfo([PATH + x for x in os.listdir(PATH) if '.html' in x])

l.close()



f = open(PATH + 'RT_' + strftime("%Y-%m-%d_%H-%M-%S") + '.txt', 'w', encoding = 'utf-8')
f.write('Movie_ID' + '|' + 'Movie_Name' + '|' + 'Audience_Score' + '|' + 'Tomatometer' + '|' + 'Cast' + '|' + 'Movie_Summary' + '|' + 'In_Theaters_Release_Date' + '|' + 'On_Disc_Streaming_Date' + '|' + 'Genre' + '|' + 'Studio' + '|' + 'Directed By' + '|' + 'Runtime' + '|' + 'Box Office' + '|' + 'Rating' + '|' + 'Written By' + '|' + 'Critics_AvgRating' + '|' + 'Audience_AvgRating' + '|' + 'Critics_ReviewsCounted' + '|' + 'Audience_ReviewsCounted' + '|' + 'Franchise' + '|' + 'Critics_Reviews' + '|' + 'Audience_Reviews' + '|' + 'Critics_Consensus' + '\n')

for x in AIA:
	f.write(x)

f.close()

print("--- %s seconds ---" % (time.clock() - start_time))




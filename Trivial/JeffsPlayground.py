import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("/Users/CalvinCao/Local/RT/RT_All_Gen1_12_Movie_Page_Sources_HTML/0814255.html"),'lxml')
def r():
	for i in range(len(soup.findAll('div',{'class':re.compile('meta-label subtle')}))):
		# a.append(soup.findAll('div',{'class':re.compile('meta-value')})[i].text.strip())
		# b.append(soup.findAll('div',{'class':re.compile('meta-label subtle')})[i].text.strip()[:-1].replace(' ','_').replace('/','_'))
		A[str(soup.findAll('div',{'class':re.compile('meta-label subtle')})[i].text.strip()[:-1].replace(' ','_').replace('/','_'))] = soup.findAll('div',{'class':re.compile('meta-value')})[i].text.strip()
		
# a = []
# b = []
A = {}
r()
print(A)
# print(b)
# print(a)
# print(len(a))
# print(RA)
# RA = Rating.replace(' ', '') #combine words
# print(RA)
# soup.findAll('div',{'class':re.compile('meta-value')})[i].text.strip()
# RA = soup.findAll('div',{'class':re.compile('meta-value')})[0].text.strip()
# print(RA)

# print(soup.findAll('div',{'class':re.compile('meta-label subtle')})[0].text.strip()[:-1].replace(' ','_').replace('/','_'))
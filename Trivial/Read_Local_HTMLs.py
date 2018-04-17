from bs4 import BeautifulSoup
soup = BeautifulSoup(open("C:/Local/RT/Random100/3-backyards.html"), "html.parser")
# Do your things below (Example):
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
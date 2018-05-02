#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:24:33 2018

@author: dyna
"""

pageLink = 'https://www.rottentomatoes.com/m/blockers'
import requests
from lxml import etree
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
headers={"User-Agent":user_agent}  #请求头,headers是一个字典类型

html = requests.get(pageLink,headers=headers).content
selector = etree.HTML(html)
tomatometers= selector.xpath('//*[@id="scoreStats"]/div[2]')
for tomatometer in tomatometers:
    reviews_counted=tomatometer.xpath('//*[@id="scoreStats"]/div[2]/span[2]')
    print (reviews_counted[0].text)
    
audiences=selector.xpath('//*[@id="scorePanel"]/div[2]/div[2]')
for audience in audiences:
    users_rating_text=audience.xpath('//*[@id="scorePanel"]/div[2]/div[2]/div[2]/text()')
    users_rating=users_rating_text[1].split()[0]
    print(users_rating)
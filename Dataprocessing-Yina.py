#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 09:29:41 2018

@author: dyna
"""

import pandas as pd
import pandas_profiling
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#read txt
df=pd.read_table('/Users/dyna/Desktop/sample.txt')
df.info()
df.head()

#change type
df['audience_score']= df['audience_score'].str.strip("%").astype(int)
df['critic_score']=df['critic_score'].str.strip("%").astype(int)
df['gap']=df['critic_score']-df['audience_score']
df['Runtime']=df['Runtime'].str.strip("minutes").astype(int)
df['Box Office']=df['Box Office'].str.strip("$").astype(str)
del df['actor_links','Box Office']

#Date transformation
import calendar
import timestring
df['Release_Date'] = ''
df['Release_Month'] = ''
df['Release_Day'] = ''
df['Weekend_Release'] = ''
df['Holiday_Release'] = ''

holidays = ['1-1', 
            #Memorial Day
            '5-25', '5-26', '5-27', '5-28', '5-29', '5-30', '5-31', 
            #Independence Day
            '7-4', 
            # Labor Day
            '9-1', '9-2', '9-3', '9-4', '9-5', '9-6', '9-7', 
            #Thanksgiving Day
            '11-22', '11-23', '11-24', '11-25', '11-26', '11-27', '11-28', 
            #Christmas Day
            '12-25']

for i in range(0, 49):
    try:
        df['Release_Date'][i] = timestring.Date(df['In Theaters'][i])
        df['Release_Month'][i] = timestring.Date(df['In Theaters'][i]).month
        df['Release_Day'][i]= calendar.day_name[timestring.Date(df['In Theaters'][i]).weekday]
        
        if str(df['Release_Day'][i]) == 'Friday' or str(df['Release_Day'][i]) == 'Saturday' or str(df['Release_Day'][i]) == 'Sunday':
            df['Weekend_Release'][i] = 1
        else:
            df['Weekend_Release'][i] = 0
            
        if str(timestring.Date(df['In Theaters'][i]).month) + '-' + str(timestring.Date(df['In Theaters'][i]).day) in holidays:
            df['Holiday_Release'][i] = 1
        else:
            df['Holiday_Release'][i] = 0

    except:
        pass

#Evaluate for synopsis
from textblob import TextBlob
bloblist_desc = list()

df_review_str=df['synopsis'].astype(str)
for row in df_review_str:
    blob = TextBlob(row)
    bloblist_desc.append((row,blob.sentiment.polarity, blob.sentiment.subjectivity))
    df_polarity_desc = pd.DataFrame(bloblist_desc, columns = ['summary','sentiment','polarity'])
 
def f(df_polarity_desc):
    if df_polarity_desc['sentiment'] > 0:
        val = "1"
    elif df_polarity_desc['sentiment'] == 0:
        val = "0"
    else:
        val = "-1"
    return val

df['synopsis_sc'] = df_polarity_desc.apply(f, axis=1)


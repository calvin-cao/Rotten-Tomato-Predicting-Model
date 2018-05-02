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

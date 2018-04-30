#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 00:29:43 2018

@author: dyna
"""

import re
import pandas as pd
import pandas_profiling
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import calendar
import timestring
from textblob import TextBlob



### Read everything ###
PATH = input('\nWhere is eveyrthing?\n') # Input root folder directory
if len(PATH) < 1:
    PATH = "/Users/dyna/Documents/GitHub/Rotten-Tomato-Predicting-Model/The_Model/"

TRAIN = input("What's your train set called?\n") # Input train set file name
if len(TRAIN) < 1:
    TRAIN = 'test.txt'

TEST = input("And what's your test set called?\n") # Input test set file name
if len(TEST) < 1:
    TEST = ''

# 1. Read train set:
print("Reading train set:")
fh0 = open(PATH + TRAIN, 'r', encoding = 'utf-8')
"""
test = {} # Define train set dictionary
i = 0
for line in fh0:
    if i == 0:
        i += 1
        continue
    if not i == 0:
        i += 1
        line = line.strip().split('\t')
        test[str(line[0])] = line[1:]
fh0.close()
print(str(len(test)) + ' lines have successfully loaded.')
"""
print("Train set read\n")
# Train set read

# 2. Read test set:
print("Reading test set:")


print("Test set read\n")
# Test set read

# 3. Read additional data files:
"""
What we have:
1. D1.txt
2. D2.txt
3. D3.txt
4. Additional _data_1.txt
5. Additional_data_1.txt
6. GC_pair_versus_CS.txt
"""
print("Reading additional data files:")
fh1 = open(PATH + 'D1.txt', 'r', encoding = 'utf-8')
# Read
fh1.close()

fh2 = open(PATH + 'D2.txt', 'r', encoding = 'utf-8')
# Read
fh2.close()

fh3 = open(PATH + 'D3.txt', 'r', encoding = 'utf-8')
# Read
fh3.close()

fh4 = open(PATH + 'Addtional_data_1.txt', 'r', encoding = 'utf-8')
# Read
fh4.close()

fh5 = open(PATH + 'Addtional_data_2.txt', 'r', encoding = 'utf-8')
# Read
fh5.close()

fh6 = open(PATH + 'GC_pair_versus_CS.txt', 'r', encoding = 'utf-8')
# Read
fh6.close()


print("Additional files read\n")
# Additional files read
print("File read complete. Proceed")



### Feature Retract ###
# Feature 1-3:
df = pd.read_table(PATH + TRAIN)
df['audience_score'] = df['audience_score'].replace('None', np.nan)
df['audience_score'] = df['audience_score'].str.strip("%")
df['audience_score'] = df['audience_score'].astype(float)
df['critic_score'] = df['critic_score'].replace('None', np.nan)
df['critic_score'] = df['critic_score'].str.strip("%")
df['critic_score'] = df['critic_score'].astype(float)
del df['actor_links']
del df['Box Office']
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

# Feature 4:
bloblist_desc = list()
df_review_str = df['synopsis'].astype(str)
for row in df_review_str:
    blob = TextBlob(row)
    bloblist_desc.append((row,blob.sentiment.polarity, blob.sentiment.subjectivity))
    df_polarity_desc = pd.DataFrame(bloblist_desc, columns = ['summary','sentiment','polarity'])
def f(df_polarity_desc):
    if df_polarity_desc['sentiment'] > 0:
        val = "2"
    elif df_polarity_desc['sentiment'] == 0:
        val = "1"
    else:
        val = "0"
    return val
df['synopsis_sc'] = df_polarity_desc.apply(f, axis=1)

df['Runtime']=df['Runtime'].replace('None', np.nan)
df['Runtime']=df['Runtime'].str.strip("minutes")
df['Runtime']=df['Runtime'].astype(float)

df['Holiday_Release']=df['Holiday_Release'].replace('', np.nan)
df['Holiday_Release']=df['Holiday_Release'].fillna(2.0)
df['Holiday_Release']=df['Holiday_Release'].astype(float)
df['Weekend_Release']=df['Holiday_Release'].replace('', np.nan)
df['Weekend_Release']=df['Holiday_Release'].fillna(2.0)
df['Weekend_Release']=df['Holiday_Release'].astype(float)
df['synopsis_sc']=df['synopsis_sc'].astype(int)

df['Release_Month']=df['Release_Month'].replace('', np.nan)
df['Release_Month']=df['Release_Month'].fillna(2.0)
df['Release_Month']=df['Release_Month'].astype(float)

dummies_Studio=pd.get_dummies(df['Studio'],prefix ='Studio')
dummies_Wtitten=pd.get_dummies(df['Written By'],prefix ='Written By')
dummies_Directed=pd.get_dummies(df['Directed By'],prefix='Directed By') 
dummies_rating=pd.get_dummies(df['Rating'],prefix='Rating')
dummies_genre=pd.get_dummies(df['Genre'],prefix='Genre')
df=pd.concat([df,dummies_Studio,dummies_Wtitten,dummies_rating,dummies_genre],axis=1)

del df['actor_names']
del df['synopsis']
del df['In Theaters']
del df['Genre']
del df['Studio']
del df['Directed By']
del df['Rating']
del df['Written By']
del df['Release_Date']
del df['Release_Day']

df['difference']=df['critic_score']-df['audience_score']
from sklearn import *
import sklearn
from multiprocessing import Pool, cpu_count
import gc; gc.enable()
df=df.fillna(0)
cols = [c for c in df.columns if c not in ['movie_id','difference']]
test_size = 0.4; seed = 123
features = df[cols]
labels = df['difference'].values
df_train, df_test, label_train, label_test = cross_validation.train_test_split(df, labels, test_size=test_size, 
random_state=seed)
data_train = df_train[cols]
data_test = df_test[cols]

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(random_state=49)                                          
clf.fit(data_train,label_train)
#use hard voting to predict (majority voting)
pred=clf.predict(data_test) 
#print accuracy
print (accuracy_score(pred,label_test))




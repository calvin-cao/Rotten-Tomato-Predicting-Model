# -*- coding: utf-8 -*-
"""
@author: smit-mehta
"""

from sklearn import linear_model
import numpy as np

import calendar
import timestring
import pandas as pd
import re


df=pd.read_csv('test_2018-04-29_18-08-57.txt', sep='\t')
df=pd.DataFrame(data=df)



df['Release_Date'] = ''
df['Release_Month'] = ''
df['Release_Day'] = ''
df['Weekend_Release'] = ''
df['Holiday_Release'] = ''
df['Release_Type'] = ''
#df['Difference'] = ''


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


for i in range(0, len(df.index) - 1):
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
            
        temp = re.sub('[^a-zA-Z]',' ',df['In Theaters'][i])
        temp = re.sub(' +',' ',temp).strip()
        df['Release_Type'][i] = str(temp[4:])

    except:
        df['Weekend_Release'][i] = 0
        df['Holiday_Release'][i] = 0
        df['Release_Type'][i] = 'wide'
        



df['audience_score'] = df['audience_score'].replace('None', np.nan)
df['audience_score'] = df['audience_score'].str.strip("%")
df['audience_score'] = df['audience_score'].astype(float)
df['critic_score'] = df['critic_score'].replace('None', np.nan)
df['critic_score'] = df['critic_score'].str.strip("%")
df['critic_score'] = df['critic_score'].astype(float)
del df['actor_links']
del df['Box Office']



df['Runtime']=df['Runtime'].replace('None', np.nan)
df['Runtime']=df['Runtime'].str.strip("minutes")
df['Runtime']=df['Runtime'].astype(float)

df['Holiday_Release']=df['Holiday_Release'].replace('', np.nan)
df['Holiday_Release']=df['Holiday_Release'].fillna(2.0)
df['Holiday_Release']=df['Holiday_Release'].astype(float)
df['Weekend_Release']=df['Holiday_Release'].replace('', np.nan)
df['Weekend_Release']=df['Holiday_Release'].fillna(2.0)
df['Weekend_Release']=df['Holiday_Release'].astype(float)
#df['synopsis_sc']=df['synopsis_sc'].astype(int)

#df['Release_Month']=df['Release_Month'].replace('', np.nan)
#df['Release_Month']=df['Release_Month'].fillna(2.0)
#df['Release_Month']=df['Release_Month'].astype(float)

#get dummies to category variable
dummies_Studio=pd.get_dummies(df['Studio'],prefix ='Studio')
dummies_Wtitten=pd.get_dummies(df['Written By'],prefix ='Written By')
dummies_Directed=pd.get_dummies(df['Directed By'],prefix='Directed By') 
dummies_rating=pd.get_dummies(df['Rating'],prefix='Rating')
dummies_genre=pd.get_dummies(df['Genre'],prefix='Genre')
dummies_release_type = pd.get_dummies(df['Release_Type'],prefix='Release_Type')
df=pd.concat([df,dummies_Studio,dummies_Wtitten,dummies_rating,dummies_genre,dummies_release_type],axis=1)

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
del df['Release_Month']
del df['Release_Type']

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




lm = linear_model.LinearRegression()
model = lm.fit(data_train,label_train)


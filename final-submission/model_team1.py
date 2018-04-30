# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:34:41 2018
@author：Team 1

"""

## Chunk 1 --------------------------------

import numpy as np
from textblob import TextBlob
import calendar
import timestring
import pandas as pd
import re
from sklearn import *
import sklearn

#Please set your working directory to point where the raw dataset file is
#Reading Data
df=pd.read_csv('rotten.txt', sep='\t')
df=pd.DataFrame(data=df)


## Chunk 2 --------------------------------

#Generating features
df['Release_Date'] = ''
df['Release_Month'] = ''
df['Release_Day'] = ''
df['Weekend_Release'] = ''
df['Holiday_Release'] = ''
df['Release_Type'] = ''

holidays = ['1-1', 
            #Memorial Day
            '5-25', '5-26', '5-27', '5-28', '5-29', '5-30', '5-31', 
            #Independence Day
            '7-4', 
            #Labor Day
            '9-1', '9-2', '9-3', '9-4', '9-5', '9-6', '9-7', 
            #Thanksgiving Day
            '11-22', '11-23', '11-24', '11-25', '11-26', '11-27', '11-28', 
            #Christmas Day
            '12-25']

## Chunk 3 --------------------------------

for i in range(0, len(df.index) - 1):
    try:
        #Identifying the month, and day of the week for the release
        df['Release_Date'][i] = timestring.Date(df['In Theaters'][i])
        df['Release_Month'][i] = timestring.Date(df['In Theaters'][i]).month
        df['Release_Day'][i]= calendar.day_name[timestring.Date(df['In Theaters'][i]).weekday]
        
        #Creating a flag for weekend releases
        if str(df['Release_Day'][i]) == 'Friday' or str(df['Release_Day'][i]) == 'Saturday' or str(df['Release_Day'][i]) == 'Sunday':
            df['Weekend_Release'][i] = 1
        else:
            df['Weekend_Release'][i] = 0
        
        #Creating a flag for Holiday releases
        if str(timestring.Date(df['In Theaters'][i]).month) + '-' + str(timestring.Date(df['In Theaters'][i]).day) in holidays:
            df['Holiday_Release'][i] = 1
        else:
            df['Holiday_Release'][i] = 0
        
        #Identifying the type of release, whether wide or limited
        temp = re.sub('[^a-zA-Z]',' ',df['In Theaters'][i])
        temp = re.sub(' +',' ',temp).strip()
        df['Release_Type'][i] = str(temp[4:])

    except:
        df['Weekend_Release'][i] = 0
        df['Holiday_Release'][i] = 0
        df['Release_Type'][i] = 'wide'
        
## Chunk 4 --------------------------------

#Identifying the sentiment of the synopsis/summary of the movie and assigning 2 for positive while 1 for negative      
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
 
        
## Chunk 5 --------------------------------

#Cleaning up the data
df['audience_score'] = df['audience_score'].replace('NONE', np.nan)
df['audience_score'] = df['audience_score'].str.strip("%")
df['audience_score'] = df['audience_score'].astype(float)
df['critic_score'] = df['critic_score'].replace('NONE', np.nan)
df['critic_score'] = df['critic_score'].str.strip("%")
df['critic_score'] = df['critic_score'].astype(float)
del df['actor_links']
del df['Box Office']

df['Runtime']=df['Runtime'].replace('NONE', np.nan)
df['Runtime']=df['Runtime'].str.strip("minutes")
df['Runtime']=df['Runtime'].astype(float)

df['Holiday_Release']=df['Holiday_Release'].replace('', np.nan)
df['Holiday_Release']=df['Holiday_Release'].fillna(2.0)
df['Holiday_Release']=df['Holiday_Release'].astype(float)
df['Weekend_Release']=df['Holiday_Release'].replace('', np.nan)
df['Weekend_Release']=df['Holiday_Release'].fillna(2.0)
df['Weekend_Release']=df['Holiday_Release'].astype(float)
df['synopsis_sc']=df['synopsis_sc'].astype(int)


## Chunk 6 --------------------------------

#Create dummy values for the categorical variables
dummies_Studio=pd.get_dummies(df['Studio'],prefix ='Studio')
#dummies_Wtitten=pd.get_dummies(df['Written By'],prefix ='Written By')
#dummies_Directed=pd.get_dummies(df['Directed By'],prefix='Directed By') 
##Removing the dummy values for the Writer and Director of the movie had almost no impact on the MSE and R-squared
##and hence we removed them from the model
dummies_rating=pd.get_dummies(df['Rating'],prefix='Rating')
dummies_genre=pd.get_dummies(df['Genre'],prefix='Genre')
dummies_release_type = pd.get_dummies(df['Release_Type'],prefix='Release_Type')
df=pd.concat([df,dummies_Studio,dummies_rating,dummies_genre,dummies_release_type],axis=1)


#Removing the unused variables
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


#Create dependent variable
df['difference']=df['critic_score']-df['audience_score']


## Chunk 7 --------------------------------

#Splitting the data into train and test
df=df.fillna(0)
cols = [c for c in df.columns if c not in ['movie_id','difference']]
features = df[cols]
labels= df['difference'].values

test_size = 0.4; seed = 123
df_train, df_test, label_train, label_test = cross_validation.train_test_split(df, labels, test_size=test_size, random_state=seed)
data_train = df_train[cols]
data_test = df_test[cols]


#Training the Model and fitting it on the training data
from sklearn import tree
clf = tree.DecisionTreeRegressor()

clf.fit(data_train, label_train)  
pred=clf.predict(data_test)

#Printing the MSE and the R-squared
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

print('MSE',mean_squared_error(label_test, pred))  
print('R2',r2_score(label_test, pred))






'''
#Our attempt at training other models

#Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(data_train, label_train)  
pred=clf.predict(data_test)
#Calculated MSE: 1278.50523295


#Nearest Centroid model
from sklearn.neighbors.nearest_centroid import NearestCentroid
clf = NearestCentroid()
from sklearn.metrics import mean_squared_error
print('MSE',mean_squared_error(label_test, pred)) 
#Calculated MSE: 222 


#Neural Network's MLP Classifier
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(random_state=49) 
from sklearn.metrics import mean_squared_error
print('MSE',mean_squared_error(label_test, pred)) 
#Calculated MSE: 27.583220796 

'''


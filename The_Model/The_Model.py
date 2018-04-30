### Import everything ###
import re
import time
import pandas as pd
import pandas_profiling
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import calendar
import timestring
from textblob import TextBlob
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn import linear_model
from sklearn import *
import sklearn
from multiprocessing import Pool, cpu_count
import gc; gc.enable()
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score



### Read everything ###
def ReadEverything(PATH, TRAIN, TEST):
    PATH = str(PATH)
    TRAIN = str(TRAIN)
    TEST = str(TEST)
    # 1. Read additional data files:
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
    fh1.close()
    fh2 = open(PATH + 'D2.txt', 'r', encoding = 'utf-8')
    fh2.close()
    fh3 = open(PATH + 'D3.txt', 'r', encoding = 'utf-8')
    fh3.close()
    fh4 = open(PATH + 'Addtional_data_1.txt', 'r', encoding = 'utf-8')
    fh4.close()
    fh5 = open(PATH + 'Addtional_data_2.txt', 'r', encoding = 'utf-8')
    fh5.close()
    fh6 = open(PATH + 'GC_pair_versus_CS.txt', 'r', encoding = 'utf-8')
    GC_pair = {}
    i = 0
    for line in fh6:
        if i == 0:
            i += 1
            continue
        if not i == 0:
            i += 1
            line = line.strip().split('\t')
            GC_pair[str(line[0])] = line[1:]
    fh6.close()
    # Additional files read
    print("File read complete. Proceed.")
    
    ### Feature Retract ###
    ## For train set ##
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
    # Feature 5:

    ## For test set ##
    df_test = pd.read_table(PATH + TEST)
    df_test['audience_score'] = df_test['audience_score'].replace('None', np.nan)
    df_test['audience_score'] = df_test['audience_score'].str.strip("%")
    df_test['audience_score'] = df_test['audience_score'].astype(float)
    df_test['critic_score'] = df_test['critic_score'].replace('None', np.nan)
    df_test['critic_score'] = df_test['critic_score'].str.strip("%")
    df_test['critic_score'] = df_test['critic_score'].astype(float)
    del df_test['actor_links']
    del df_test['Box Office']
    df_test['Release_Date'] = ''
    df_test['Release_Month'] = ''
    df_test['Release_Day'] = ''
    df_test['Weekend_Release'] = ''
    df_test['Holiday_Release'] = ''
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
            df_test['Release_Date'][i] = timestring.Date(df_test['In Theaters'][i])
            df_test['Release_Month'][i] = timestring.Date(df_test['In Theaters'][i]).month
            df_test['Release_Day'][i]= calendar.day_name[timestring.Date(df['In Theaters'][i]).weekday]
            if str(df_test['Release_Day'][i]) == 'Friday' or str(df['Release_Day'][i]) == 'Saturday' or str(df_test['Release_Day'][i]) == 'Sunday':
                df_test['Weekend_Release'][i] = 1
            else:
                df_test['Weekend_Release'][i] = 0
            if str(timestring.Date(df_test['In Theaters'][i]).month) + '-' + str(timestring.Date(df_test['In Theaters'][i]).day) in holidays:
                df_test['Holiday_Release'][i] = 1
            else:
                df_test['Holiday_Release'][i] = 0
        except:
            pass
    # Feature 4:
    bloblist_desc = list()
    df_review_str = df_test['synopsis'].astype(str)
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
    df_test['synopsis_sc'] = df_polarity_desc.apply(f, axis=1)
    # Feature 5:

    ## Transfer dataframe to normal dictionary form (KEY = movie_id, VALUE = [columns]):
    A = df.to_dict('records')
    train = {}
    for x in A:
        a = []
        for s in x:
            a.append(x[s])
        train[str(a[0])] = []
        for n in a[1:]:
            train[str(a[0])].append(n)
    del(A)
    B = df_test.to_dict('records')
    test = {}
    for x in B:
        a = []
        for s in x:
            a.append(x[s])
        test[str(a[0])] = []
        for n in a[1:]:
            test[str(a[0])].append(n)
    del(B)

    print('\nRead complete. Prceed.\n')
    return df, df_test, train, test, GC_pair

df, df_test, train, test, GC_pair = ReadEverything("C:/Users/calvi/Documents/GitHub/RottenTomatoPredictingModel/The_Model/", "test.txt", "sample.txt")


# Separate test.txt 7-3:




"""
### Calvin's Model v0.1 ###
# Train:

GC_pair_temp = dict()
for every_movie in train:
    GE = train[str(every_movie)][6].strip().split(',') # Genre
    CA = train[str(every_movie)][2].strip().split(',') # Cast
    CS = train[str(every_movie)][1] # Critics_Score
    AS = train[str(every_movie)][0] # Audience_Score
    A = []
    for x in CA:
        for s in GE:
            A.append(str(x) + ' + ' + str(s))
    for a in A:
        if str(a) in GC_pair_temp:
            try:
                if not CS:
                    continue
                else:
                    GC_pair_temp[str(a)].append(str(CS))
            except:
                continue
        elif not str(a) in GC_pair_temp:
            GC_pair_temp[str(a)] = []
            try:
                if not CS:
                    continue
                else:
                    GC_pair_temp[str(a)].append(str(CS))
            except:
                continue
        else:
            continue
    GE,CA,BO,CS,AS = None, None, None, None, None
GC_pair = dict()
for x in GC_pair_temp:
    l = 0
    s = 0.0
    l = len(GC_pair_temp[x])
    if l == 0:
        continue
    if not l == 0:
        for v in GC_pair_temp[x]:
            if v == 'None':
                continue
            try:
                ad = int(v)
            except:
                continue
            else:
                s = s + float(ad)
        GC_pair[x] = [s/l, len(GC_pair_temp[x])]
del(GC_pair_temp)


# Define
# [2] = Cast, [6] = Genre
def GCP_Lookup(Dict, Pair):
    for every_movie in Dict:
        GE = Dict[str(every_movie)][6].split(',') # Genre
        CA = Dict[str(every_movie)][2].split(',') # Cast
        P = []
        for x in CA:
            for s in GE:
                P.append(str(x) + ' + ' + str(s))
        S = []
        for pair in P:
            if pair in Pair:
                S.append(Pair[pair])
        SumWeight = 0
        for s in S:
            SumWeight += float(s[1])
        Prediction = 0.0
        for s in S:
            Prediction += float(s[0])*float(s[1])/SumWeight
        print(Prediction)
    return

# Predict

GCP_Lookup(test, GC_pair)
for x in test:
    print(test[x][1])
"""
### Module import ###
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
    PATH = "C:/Users/calvi/Documents/GitHub/RottenTomatoPredictingModel/The_Model/"

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

# Feature 5:


# Transfer dataframe to normal dictionary form (KEY = movie_id, VALUE = [columns]):
A = df.to_dict('records')
test = {}
for x in A:
    a = []
    for s in x:
        a.append(x[s])
    test[str(a[0])] = []
    for n in a[1:]:
        test[str(a[0])].append(n)

for x in test['10']:
    print(str(x))


# -*- coding: utf-8 -*-
"""
@author: smit-mehta
"""
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
    


#df.head(10)


 



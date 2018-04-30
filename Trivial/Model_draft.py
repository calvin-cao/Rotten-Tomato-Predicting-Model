# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 19:59:03 2018

@author: Nishita
"""

import csv
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
enc = OneHotEncoder()
# initialize variables
column = []
data_val = []
progress = 0
scores = []

#variables for calculating error margin
rf_error_margin = 0
dt_error_margin = 0
nb_error_margin = 0
svm_error_margin = 0
count = 0

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
train =pd.read_table('C:/Users/Nishita/Documents/Spring 2018/BIA 660 Web Aanlytics - Lappas/Final Project/train_f.txt')
#test = read_csv('test.csv')

# convert the float scores to int. Multiplying by 10 helps us keep the decimal
encoded_data = enc.fit(train)


#cols_to_transform = [ 'actor_names', 'Genre', 'Studio', 'Directed By', 'Written By']
#df_with_dummies = pd.get_dummies( columns = cols_to_transform )
"""i = 0
while i < len(label):
    scores.append(int (float(label[i]) * 10))
    i += 1;
"""

# Gaussian Naive Bayes
nb_clf = GaussianNB()
nb_clf.fit(encoded_data, scores)

# Random Forest
rf_clf = RandomForestClassifier(n_estimators=100)
rf_clf.fit(encoded_data, scores)

# Decision Tree
dt_clf = tree.DecisionTreeClassifier()
dt_clf.fit(encoded_data, scores)


# SVM classifier
svm_clf = svm.SVC(kernel = 'linear')
svm_clf.fit(encoded_data, scores)

with open('train.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        column.append(row['movie_id'])
        column.append(row['actor_names'])
        column.append(row['synopsis'])
        column.append(row['In Theaters'])
        column.append(row['Genre'])
        column.append(row['Studio'])
        column.append(row['Directed By'])
        column.append(row['Runtimes'])
        column.append(row['Box Office'])
        column.append(row['Rating'])
        column.append(row['Written By'])
        data_val.append(column)
        test_data = encode(data_val)

        # calculate error margin for SVM
        #svm_error_margin += abs((svm_clf.predict (test_data)/10.0) - (float(row['imdb_score'])))

        # calculate error margin for Naive Bayes
        nb_error_margin += abs((nb_clf.predict (test_data)/10.0) - (float(row['imdb_score'])))
        
        # calculate error margin for Random Forest
        rf_error_margin += abs((rf_clf.predict (test_data)/10.0) - (float(row['imdb_score'])))
        
        # calculate error margin for Decision Tree
        dt_error_margin += abs((dt_clf.predict (test_data)/10.0) - (float(row['imdb_score'])))

        count += 1
        column = []
        data_val = []

# Print the error margin

print("Error margin for Naive Bayes: %0.2f" % (nb_error_margin/count))

print("Error margin for Random Forest: %0.2f" % (rf_error_margin/count))

print("Error margin for Decision Tree: %0.2f" % (dt_error_margin/count))

#print("Error margin for SVM: %0.2f" % (svm_error_margin/count))

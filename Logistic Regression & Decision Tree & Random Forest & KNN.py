# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:46:50 2024

@author: mostafa
"""

import pandas as pd
import numpy as np

df = pd.read_csv("heart.csv")

print(df.head())

print(df.info())

print(df.isnull().sum())

print(df.duplicated().sum())

# df.drop_duplicates(inplace = True)

x = df.drop('target', axis = 1)
# x = df.iloc[:, :-1]
y = df['target']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25,
                                                    random_state=41)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(max_iter = 1000)
lr.fit(x_train, y_train)
    
y_pred = lr.predict(x_test)

from sklearn.metrics import accuracy_score
########################################################################
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth = 10)
dt.fit(x_train, y_train)


y_pred = dt.precdit(x_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbots = 5)
knn.fit(x_train, y_train)
########################################################################

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators = 5)









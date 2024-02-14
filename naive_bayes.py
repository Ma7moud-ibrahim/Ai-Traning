import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score, confusion_matrix

df = pd.read_csv("heart.csv")
print(df.shape)
print(df.head())
print(df.tail())
print(df.describe())
print(df.corr)
print(df.info())
print(df.isnull().sum())

x = df.drop('target', axis=1)
y = df['target']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=41)

# Naive Bayes
model_nb = GaussianNB()
model_nb.fit(x_train, y_train)  
y_pred_nb = model_nb.predict(x_test)

print("N Accuracy:", accuracy_score(y_test, y_pred_nb))
print("N Confusion Matrix:\n", confusion_matrix(y_test, y_pred_nb))

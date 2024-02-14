import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

df = pd.read_csv('bike_buyers.csv', sep="\t")

print(df.head())
print(df.info())
print(f"Null values:\n{df.isnull().sum()}")
print(f"Duplicated rows: {df.duplicated().sum()}")

df['Marital Status'] = df['Marital Status'].fillna(df['Marital Status'].mode()[0])
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Home Owner'] = df['Home Owner'].fillna(df['Home Owner'].mode()[0])
df.fillna(df.select_dtypes(include=np.number).mean(), inplace=True)

print(f"Null values:\n{df.isnull().sum()}")
print(f"Duplicated rows: {df.duplicated().sum()}")

object_columns = ['Marital Status', 'Gender', 'Education', 'Occupation', 'Home Owner', 'Region']
df = pd.get_dummies(df, columns=object_columns, drop_first=True)

x = df.drop('Purchased Bike', axis=1)
y = df['Purchased Bike']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=41)

lr = LogisticRegression(max_iter=5000)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

dt = DecisionTreeClassifier(max_depth=10)
dt.fit(x_train, y_train)
y_pred_dt = dt.predict(x_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred_knn = knn.predict(x_test)

rf = RandomForestClassifier(n_estimators = 5)
RandomForest =  rf.fit(x_train, y_train)
y_pred_rf = RandomForest.predict(x_test)


print(f"Logistic  Regression Accuracy: {accuracy*100}%")
print("Decision Tree Accuracy: ", accuracy_score(y_test, y_pred_dt))
print("KNN Accuracy: ", accuracy_score(y_test, y_pred_knn))
print("Random Forest Accuracy: ", accuracy_score(y_test, y_pred_rf))

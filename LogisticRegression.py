import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
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

# max_iter = increase
lr = LogisticRegression(max_iter=5000)
lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score, confusion_matrix

df = pd.read_csv("E:\Codes\Ai Traning\SalaryData2.csv")
print(df.shape)
print(df.head())
print(df.tail())
print(df.describe())
print(df.corr)
print(df.info())
print(df.isnull().sum())
df['Education Level'] = df['Education Level'].fillna(df['Education Level'].mode()[0])
df['Years of Experience'] = df['Years of Experience'].fillna(df['Years of Experience'].mode()[0])
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df.fillna(df.select_dtypes(include=np.number).mean(), inplace=True)

df.drop("Job Title", inplace=True, axis=1)

object_columns = ['Education Level', 'Gender']
df = pd.get_dummies(df, columns=object_columns, drop_first=True)

x = df.drop('Salary', axis=1)
y = df['Salary']

poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_poly, y, test_size=0.25, random_state=41)

# Linear Regression
model_lr = LinearRegression()
model_lr.fit(x_train, y_train)
y_pred_lr = model_lr.predict(x_test)

print("L Mean Squared Error:", mean_squared_error(y_test, y_pred_lr))
print("L Mean Absolute Error:", mean_absolute_error(y_test, y_pred_lr))



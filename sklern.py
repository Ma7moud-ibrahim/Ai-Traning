import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import svm
from sklearn.metrics import confusion_matrix,accuracy_score,ConfusionMatrixDisplay
df = pd.read_csv('svm.csv')

print(df.shape)
print(df.head())
print(df.tail())
print(df.describe())
# print(df.corr())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df['Name'] = df['Name'].fillna(df['Name'].mode()[0])
df['Sex'] = df['Sex'].fillna(df['Sex'].mode()[0])
df['Ticket'] = df['Ticket'].fillna(df['Ticket'].mode()[0])
df['Cabin'] = df['Cabin'].fillna(df['Cabin'].mode()[0])
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

object_columns = ['Name', 'Sex', 'Ticket', 'Embarked', 'Cabin']
df = pd.get_dummies(df, columns=object_columns, drop_first=True)
df.fillna(df.select_dtypes(include=np.number).mean(), inplace=True)
print(df.isnull().sum())

x = df.drop("Survived", axis=1)
y = df["Survived"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

svm_model = svm.SVC()
svm_model.fit(x_train,y_train)
y_pred = svm_model.predict(x_test)

print(confusion_matrix(y_test, y_pred))
cm = ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred), display_labels=["Died","Survived"])
cm.plot()
plt.show()

acc = accuracy_score(y_test, y_pred)
print("Accuracy: ", acc)

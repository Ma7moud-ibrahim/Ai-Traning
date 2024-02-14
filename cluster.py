import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('Clustering.csv')

print(df.shape)
print(df.head())
print(df.tail())
print(df.describe())
print(df.corr())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
x = df

distances = []

for i in range(1, 11):
    KMeans_model = KMeans(n_clusters=i)
    KMeans_model.fit(x)
    distances.append(KMeans_model.inertia_)# sum of destance

plt.plot(range(1, 11), distances)
plt.xlabel('Number of Clusters')
plt.ylabel('Distortion')
plt.title('Elbow Method for Optimal k')
plt.show()

optimal_k = int(input("Enter the optimal value of k  plot: "))

km = KMeans(n_clusters=optimal_k)
km.fit(x)
predictions = km.predict(x)

print(predictions)
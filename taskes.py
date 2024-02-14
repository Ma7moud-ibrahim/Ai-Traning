# def fun(x,y):
#     try:
#         return x/y
#     except Exception as e:
#         print(e)
#     else:
#         pass  # This block will not be executed if an exception occurred.
#     finally:
#         print("Good")
# raise ValueError("ERoytt")

# print(fun(10,2))   # Will divide 10 by  2 and print the result (5.0).
"""
#task1
class Queue:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Warning: Trying to pop from an empty queue.")
            return None

    def is_empty(self):
        return len(self.items) == 0


class OutOfRangeException(Exception):
    pass

#task2
class NamedQueue(Queue):
    all_queues = {}  

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size
        NamedQueue.all_queues[name] = self  

    def insert(self, value):
        if len(self.items) < self.size:
            super().insert(value)
        else:
            raise OutOfRangeException(f"Queue {self.name} is full, cannot insert more values.")

    def show_all_queues(self):
        print("All queues:")
        for queue_name, queue_instance in NamedQueue.all_queues.items():
            print(f"Queue Name: {queue_name}, Size: {queue_instance.size}, Items: {queue_instance.items}")

queue1 = NamedQueue(name="Queue1", size=3)
queue2 = NamedQueue(name="Queue2", size=2)

queue1.insert(1)
queue1.insert(2)
queue1.insert(3)



queue2.insert('A')
queue2.insert('B')


queue1.show_all_queues()
queue2.show_all_queues()

# my_queue = Queue()
# my_queue.insert(1)
# my_queue.insert(2)
# my_queue.insert(3)

# my_queue.print_list()
# print("Is the queue empty?", my_queue.is_empty())

# print("Popped:", my_queue.pop())
# print("Popped:", my_queue.pop())
# print("Popped:", my_queue.pop())
# print("Popped:", my_queue.pop())


import numpy as np
arr=np.full((5,5),1)
arr[1,1:-1]=0 #[row,posthion row,colom]
arr[2,1:-1]=0
arr[3,1:-1]=0

print(arr)

import pandas as pd
df = pd.read_csv("E:\Codes\Ai Traning\Iris.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.corr)
print(f"Missing is {df.isnull().sum()}")
print(df.fillna(df.mean(),inplace=True))
"""
# numberOfStudents=4
# print(type(numberOfStudents))

# sentence="""\t\tWelcome
#             Mahmoud Ebrahim 
#             in The Class"""
# print(sentence)

# age = 19.5
# print(type(age))
# print(int(age))
# age_str = str(age)
# print(type(age_str))

# x = "w e lcome" # String is immutable
# print(x[1:6:2]) # Step size
# print(x.capitalize()) # Hello, world
# print(x.split(" "))

# x = ['mostafa', 'ahmed', 'ali']
# last_element = x.pop(2)
# print(x)
# print(last_element)
# x.insert(0, "Mohammed")
# print(x)
# x.append("Khaled")
# print(x)
# print(x)
# print(x[0])
# print(x[1:])
# print(x[:2])
# print(x[1:3])
# y = ["Khaled", "Selim"]
# x.extend(y) # x = x + y
# print(x)

# Casting
# x = "3"
# x = int(x)
# print(x)
# print(type(x))

# x = [1, 2, 3, 4, 5]
# y = x # y = [1, 2, 3, 4, 5]
# y[1] = 10 # y = [1, 10, 3, 4, 5]
# print(x)
# print(y)

# y = x[:]
# y[1] = 15
# print(x)
# print(y)

# x.insert(5, 20) # The firsr argument is the index and the second one is the value you want to add.

# x.clear()
# x = [1, 2, 3, 4, 5]
# y = [num % 2 == 0 for num in x]
#print(y)

#x, y = "Orange", "Apple"
# x, y = ("Orange", "Apple")
# print(x,y)

# students = {
#     "name": "Mostafa",
#     "age": 20,
#     "emails": ["a@a.com", "a@s.com"],
#     "address": {
#         "street": "ABC",
#         "flat": 15
#         }
#     }

# a = students.get("address")
# print(a)
# print(students.get("address").get("street"))
# print(students.keys())
# print(students.values())
# students.update(name = "Aahmed", age = 20, salary = 5000)
# students.update({"name": "Ahmed", "age": 25})
# print(students.keys())
# print(students.values())

# import numpy as np

# arr = nu.array([1,2,3,4,6])
# print(arr)

# print(np.__version__)

# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5],ndmin=5)
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
# 


# arr = np.array([1.1, 2.1, 3.1])
# arr[0]=24
# newarr = arr.view()
# print(newarr)
# print(arr)

# arr = np.array([1, 2, 3, 4, 5])

# x = arr.copy()
# y = arr.view()

# print(x.base)
# print(y.base)

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.dstack((arr1, arr2))
# print(arr)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score, confusion_matrix

df = pd.read_csv("SalaryData2.csv")
print(df.shape)
print(df.head())
print(df.tail())
print(df.describe())
print(df.corr())
print(df.info())
print(df.isnull().sum())
df['Education Level'] = df['Education Level'].fillna(df['Education Level'].mode()[0])
df['Years of Experience'] = df['Years of Experience'].fillna(df['Years of Experience'].mode()[0])
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df.fillna(df.select_dtypes(include=np.number).mean(), inplace=True)
df['Job Title'].fillna('Unknown', inplace=True)

df.drop("Job Title", inplace=True, axis=1)

object_columns = ['Education Level', 'Gender']
df = pd.get_dummies(df, columns=object_columns, drop_first=True)

x = df.drop('Salary', axis=1)
y = df['Salary']

poly = PolynomialFeatures(degree=1)
x_poly = poly.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_poly, y, test_size=0.25, random_state=41)

# Linear Regression
model_lr = LinearRegression()
model_lr.fit(x_train, y_train)
y_pred_lr = model_lr.predict(x_test)

print("L Mean Squared Error:", mean_squared_error(y_test, y_pred_lr))
print("L Mean Absolute Error:", mean_absolute_error(y_test, y_pred_lr))

# Naive Bayes
model_nb = GaussianNB()
model_nb.fit(x_train, y_train)
y_pred_nb = model_nb.predict(x_test)

print("Naive Bayes - Accuracy:", accuracy_score(y_test, y_pred_nb))
print("Naive Bayes - Confusion Matrix:\n", confusion_matrix(y_test, y_pred_nb))

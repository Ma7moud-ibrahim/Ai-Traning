# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:08:21 2024

@author: mostafa
"""

x = 5.0

print(type(x))

# Identifier Rules:
# starts a - z A - Z _
# Can't Contain Punctuations.
# digits, _

# Camel Case
numberOfStudents = 5    
# Snake Case
number_of_students = 5 # Python Community

# Reserverd Words:
# and class if import is lambda except del break continue is finally

print("Welcome")

# Line Indentation
if x>5:
    print("Ok")
    print("Welcome")

x = 'Welcome to AI course'
print(type(x))
print(x)
x = "Welcome to AI course"
x = """Welome to AI Course""" # Trible quotation

name = "Hello I'm Ahmed\nI love Python" # \n = press enter
print(name)

name = """Hello 
I'm 
Ahmed
I love 
Python"""
# In trible we can define the string in multiple lines
print(name)

# Do we have multiple line comment in Python?
"""
Welcome to AI course.
We will study Python and Machine learning.
"""
name = "Ahmed"
age = 20
is_student = True # Boolean

# Strings, Numbers, Boolean, Lists, Tuples, and Dictionaries

age = 19.5
print(type(age))

print(int(age))

age_str = str(age)

print(type(age_str))
#################################################################
# String Concatenation
first_name = "Ahmed" # string
last_name = "Ali"

"""
my name is Ahmed Ali
"""

full_name = "my name is" + ' ' + first_name + ' ' + last_name

print(full_name)

salary = 5000 # Integer

full = first_name + last_name + "my salary is" + salary


# first solution --> Not Recommended
full_name = "%s %s and my salary is %d"%(first_name, last_name, salary)

# .format string --> Placeholders
full_name = "my name is {} {} and my salary is {}".format(first_name, last_name, salary)

print(full_name)


# formatted string python 3.6 --> Most common
full_name = f"my name is {first_name} {last_name} and my salary is {salary}"
############################################################################
# Mutable قابل للتعديل vs Immutable غير قابل للتعديل
x = "welcome" # String is immutable
print(x[-1])

print(x[1:5]) # Upper limit is excluded


print(x[2:]) # print from index 2 to the end of the string

print(x[:5])

print(x[1:6:2]) # Step size

# pop
x = "pop"

if x == x[::-1]:
    print("Ok")

a = "Hello, World Welcome"
print(a.upper()) # HELLO, WORLD
print(a.lower()) # hello, world

print(a.capitalize()) # Hello, world

print(a)


b = a.replace('e', 'B', 2)
print(a)
print(b)

print(a.split(" "))

###########################################################################
# Lists --> Mutable
x = []

x = ['mostafa', 'ahmed', 'ali']

x.insert(2, "Mohammed")
print(x)

# append
x.append("Khaled")
print(x)
x[0] = "John"

print(x)
print(x[0])
print(x[1:])
print(x[:2])
print(x[1:3])

y = ["Khaled", "Selim"]

x.extend(y) # x = x + y

print(x)

if x>5:
    print("Ok")
    print("Welcome")
elif x == 5:
    print("Equal")
else:
    print("x<5")

x = 6
if x%2 == 0:
    print("Even")

x = ['mostafa', 'ahmed', 'ali']
if 'mostafa' in x:
    print("Ok")

# append: insert at the end of the list.
# insert: insert at a specific index.
# extend: extend a list with another list.
last_element = x.pop(2)

print(x)
print(last_element)

for i in x: # 1st i = 'mostafa', 2nd i ='ahmed', 3rd i = 'ali'
    print(i)


c = len(x)
print()
"""
for (i = 0; i<c; i++):
    cout<<x[i]
"""
b = range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in b:
    print(i)

c = len(x) # 4
d = range(c) # [0, 1, 2, 3]

for i in d: # len(x) = 4 --> range(4)
    print(x[i])

for i in x:
    print(i)

c = len(x) # 4
a = range(c) # [0, 1, 2, 3]
for i in a:
    print(x[i])
    
for i in range(len(x)):
    print(x[i])


x = [5, 7, 9, 2, 4]
x.sort()
print(x) # تصاعدي
x.sort(reverse = True) # Descending تنازلي
print(x)

def welcome():
    print("welcome")



def summ(x, y):
    summ = x + y
    return summ

summ(5, 3)
##################################################################################################
if x<5:
    print("Ok")
    print("Welcome")

print("Ok")    
    
for i in range(5):
    print(i)


def summ(x, y):
    return x + y

# This is a single-line comment
"""
This is a multi-line comment.
"""

x = 5.0
name = "Mostafa"

# Casting
x = "3"
x = int(x)

print(type(x))
x = "Orange"
y = "Apple"
z = "Cherry"

x, y, z = "Orange", "Apple", "Cherry"

first_name = "Mostafa"
last_name = "Ahmed"
salary = 5000

full_name = first_name + last_name + salary


x = "Welcome to ITIDA" # ['W', 'e', 'l', .......]
for i in x:
    print(i)

# cout<<"Please enter your value";
# cin>>x
x = input("Please enter your value")
print(x)

x = 'welcome'
x = "welcome"
x = """welcome"""


x = "Welcome to ITIDA" # itida
if "ITIDA" in x.upper():
    print("Ok")
    
print("ITIDA" in x.upper())


print(x[2, 7])
print(x[2:])
print(x[::-1])
# here
welcome = "Welcome to ITIDA AI Course. This AI course is a good introduction"
print(welcome.count("AI"))

z = welcome.split(".")
print(z)

# formatted string

first_name = "Mostafa"
last_name = "Ahmed"
salary = 5000

full_name = f"my name is {first_name} {last_name} and my salary is {salary}"

x = [1, 2, 3, 4, 5]
y = x # y = [1, 2, 3, 4, 5]
y[1] = 10 # y = [1, 10, 3, 4, 5]
print(x)
print(y)

y = x[:]
y[1] = 15
print(x)
print(y)

x.append(7)
print(x)

x.insert(5, 20) # The firsr argument is the index and the second one is the value you want to add.

x.clear()
print(x)

x = [1, 2, 3, 4, 5]
y = x.pop(2)

# List Comprehension
x = [1, 2, 3, 4, 5, 6]
# Get the even numbers from this list and store in y.


y = []
for i in x:
    if i%2 == 0:
        y.append(i)
        
y = [i for i in x if i%2 == 0]
#####################################################
string1 = "Welcome"
x = [1, 2, 3, 4, 5]

for j in string1:
    print(j)

c = len(string1) # 7
d = range(c) # [0, 1, 2, 3, 4, 5, 6]

for i in d:
    print(string1[i])

for i in range(len(string1)): # range(7) --> [0, 1, 2 3, 4, 5, 6]
    print(string1[i])

def summ(x, y):
    summ = x + y
    return summ
#####################################################
# Tuples
# Immutable we cannot say that x[1] = 6
x = (1, 2, 3, 4, 5)
print(x[0])
print(x[1:4])
print(x[-1])
print(len(x))
print(x[1:])
print(type(x))

# To add element to a tuple:
x = list(x)
x.append(7)
x = tuple(x)

y = (1,)
print(type(y))
x, y = "Orange", "Apple"
x, y = ("Orange", "Apple")
#####################################################
# Dictionaries
students = {
    "name": "Mostafa",
    "age": 20,
    "emails": ["a@a.com", "a@s.com"],
    "address": {
        "street": "ABC",
        "flat": 15
        }
    }

c = students["emails"]
print(c)
print(students["emails"][1])

# Print the street name of the student.
print(students["address"])
print(students["address"]["street"])

print(students)
students["salary"] = 5000
print(students)

students["name"] = "Ahmed"
print(students)

print(students["names"]) # Will no work.

students["names"] = "Khaled"

print(students["emails"][1])

print(students["name"])
x = [0, 1, 2]
print(x[0])

students = ["Mostafa", 20]

print(students[0])


if "names" in students:
    # هل names موجودة ك key جوه ال dictionary اللي اسمه students
    print(students["names"])
else:
    print("the key is not found")

print(students.get("names", "Not Found"))
# The first value in get is the key you want to get its value.
# The second value passed to get function is the value
# you want to return if the given key is not found.
students = {
    "name": "Mostafa",
    "age": 20,
    "emails": ["a@a.com", "a@s.com"],
    "address": {
        "street": "ABC",
        "flat": 15
        }
    }

a = students.get("address")
print(a)
print(students.get("address").get("street"))
print(students.keys())
print(students.values())

for i in students.keys(): # ['name', 'age', 'emails', 'address', 'salary']
    print(i)

for j in students.values(): # ['Ahmed', 20, ['a@a.com', 'a@s.com'], {'street': 'ABC', 'flat': 15}, 5000]
    print(j)    

print(students.items())
####################################################################
dict_items = [('name', 'Mostafa'), 
              ('age', 20), 
              ('emails', ['a@a.com', 'a@s.com']), 
              ('address', {'street': 'ABC', 'flat': 15})]

first_name = "Mostafa"
salary = 5000
full = f"{first_name} ==> {salary}"
for i, j in students.items(): # ('age', 20)
    print(f"{i} ==> {j}")
    
for i in students.items():
    print(i)
#####################################################################
# *args and **kwargs
def summ(x, y):
    return x + y

sum1 = summ(5, 6) # Positional
print(sum1)

sum2 = summ(y = 6, x = 5) # Named
print(sum2)


# *args
def fun(*args): # args = (10, 20)
    x = len(args) # 2
    if x == 2:
        return args[0] + args[1]
    elif x == 3:
        return args[0] * args[1] * args[2]

fun(10, 20)
######################################################################
def fun(**kwargs): # args = (10, 20)
    print(kwargs)

fun(a = 10, b = 20)

students = {
    "name": "Mostafa",
    "age": 20,
    "emails": ["a@a.com", "a@s.com"],
    "address": {
        "street": "ABC",
        "flat": 15
        }
    }

students.update(name = "Ahmed", age = 20, salary = 5000)
students.update({"name": "Ahmed", "age": 25})








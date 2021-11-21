# lambda Function - Anonymous Function

area = lambda x : x*x
print(area(5))

# how to use lambda function in the normal function
def apple(unit_price):
    return(lambda number_of_apples : number_of_apples*unit_price)

x = apple(100)
print(x(8))

# filter function
number = [1,2,3,4,5,6,7,8]

def even_num(x):
    return x % 2 == 0
y = list(filter(even_num,number))
print(y)

# filter function using lambda function

number = [1,2,3,4,5,6,7,8]
y = list(filter(lambda x:x%2==0,number))
print(y)

# map function
number = [1,2,3,4,5,6,7,8]
y = list(map(lambda x:x*2, number))
print(y)

# reduce function
from functools import reduce
number = [1,2,3,4,5,6,7,8]

sum = reduce(lambda x,y:x+y,number)
print(sum)

# Decorators in python

def new(func):
    def inside(a,b):
        if b==0:
            a,b = b,a
        return func(a,b)
    return inside

def divide(a,b):
    return a/b

devide = new(divide)
print(devide(5,0))

# 2nd method
def new(func):
    def inside(a,b):
        if b==0:
            a,b = b,a
        return func(a,b)
    return inside

@new
def divide(a,b):
    return a/b

print(divide(5,0))

# __name__ function
def add(a,b):
     return a+b
print(add(3,5))
print(__name__)


def add(a,b):
    return a+b

if __name__=='__main__':
    print(add(2,3))


# Polymorphism -Method Overriding

class Parent:
     def func(self):
         print('hello')

class Child(Parent):
     def func(self):
         print('Suppa')

myObj = Child()
print(myObj.func())

# Polymorphism -Method Overloading

class Calc:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            sum = a+b+c
            print(sum)
        elif a!=None and b!=None:
            sum = a+b
            print(sum)
        else:
            sum = a
            print(sum)

myObj = Calc()
myObj.add(2,3)

# Exception Handling in python

try:
    a = int(input('Enter the first number :'))
    b = int(input('Enter the second number '))
    print(a/b)
except ZeroDivisionError as e:
    print('Cannot divide by zero:',e)
except ValueError as e:
    print('Cannot use interger value',e)
except Exception as e:
    print('something went wrong',e)
finally:
    print('bye')

# Arrays in python
from array import *
x = array('i',[2,4,5,6,7,3])
print(x)

# add the new elements in the array, This value add the last index
# this function is add the one element in the one moment
x.append(9)
print(x)
# How to add multiple elements in the array, it can use by extend function in this moment
x.extend([2,5,6,7])
print(x)

# how to add elements in the selected index
x.insert(2,21)
print(x)

# how to remove the index
x.pop(0)
print(x)

# How to remove the value without index number
x.remove(6)
print(x)

# how to join two arrays
y = array('i',[12,11,2,1,22,11])
z = x + y
print(z)

# How print array details in one by one
for i in range(len(x)):
    print(x[i])

# or

for i in x:
    print(i)

# Iterators

lst = {3,6,7,8,9}

itr = iter(lst)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break

# create own iteration

class myit:
    def __init__(self):
        self.y=2
    def __iter__(self):
        return self
    def __next__(self):
        val = self.y
        self.y+=2
        return val

myObj = myit()
itr = iter(myObj)
print(next(itr))
print(next(itr))

# Generators functions
def test(a):
    for i in a:
     yield i

y = test([2,1,1,2,3,4])
print(next(y))
print(next(y))
print(next(y))

# Multi Threading
import threading
from time import sleep
def func1():
    for i in range(5):
        print('good')
        sleep(1)

def func2():
    for i in range(5):
        print('Bye')
        sleep(1)

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t1.start()
sleep(0.2)
t2.start()

# MultiThreading with class
from threading import*
from time import sleep
class A(Thread):
    def func(self):
        for i in range(5):
            print('Hello')
            sleep(0.2)
class B(Thread):
    def func(self):
        for i in range(5):
            print('Welcome')
            sleep(0.2)
obj1 = A()
obj2 =B()
obj1.func()
sleep(0.2)
obj2.func()

# Abstract Classes and Method
from abc import ABC, abstractmethod
class Phone(ABC):
    @abstractmethod
    def func(self):
        pass

class Samsung(Phone):
    def func(self):
        pass

obj = Samsung()

# File Handling in python
x = open('test','r')
# full file read
print(x.read())
# line by line read
print(x.readline(),end='')
print(x.readline())

# Automatically file close
with open('test','r') as x:
    print(x.read())

# File write
x = open('test','w')
x.write("Supun Sulakshana")
x.close()

# Append Mode
x = open('test','a')
x.append('\nSupun Sulakshana')
x.close()

# How to images handling into the file

x = open('images/Screenshot (3).png','rb')
print(x.read())

# Os modules - remove file
import os
os.remove('test')

# import os
os.rename('test','new')

# how to find file name
print(os.path.exists('test'))

# How to check file path
print(os.path.abspath('test'))

# How file size check
print(os.path.exists('test'))

# Random numbers
import random
x = random.random()*18
print(x)

# how to generate random numbers with range
x = random.uniform(5,10)
print(x)

# Integer Numbers generate
x = random.randint(6,10)
print(x)

# Randomly choice string value
name = ['Kamal','Saman','Amal']
winner = random.choice(name)
print(winner)

# Shuffle Numbers
numbers = list(range(1,10))
random.shuffle(numbers)
print(numbers)

# Zip function
name = ['Supun','Sadun','Suyama']
age = [34,22,21]
marks = [23,12,11]
details = list(zip(name,age,marks))
print(details)

# UnZip function
unzip = list(zip(*details))
print(unzip)

# Pyramid patterns built up
for i in range(5):
    for j in range(i+1):
       print('* ', end='')
    print()
# second example
for i in range(5):
    for j in range(i-1):
        print('* ',end='')
    print()
# third example

for i in range(5):
    for j in range(5-i):
        print('* ',end='')
    for k in range(2*i+1):
        print('* ',end='')
    print()

# Heart pattern design

for row in range(6):
    for column in range(7):
        if row==0 and column%3 !=0:
            print('* ',end='')
        elif row==1 and column%3==0:
            print('* ',end='')
        elif row-column==2:
            print('* ',end='')
        elif row+column==8:
            print('* ',end='')
        else:
            print(' ',end='')
    print()

# os module
# how to find our working folder location
import os
print(os.getcwd())

# go to file location
os.chdir(r'C:\Users\supun\PycharmProjects\pythonPart2')

print(os.getcwd())

# Directly list
print(os.listdir())

# create new folder
os.mkdir("new")

# how to remove files in  folder

os.rmdir('new/')

# how to folder rename
os.rename('new','welcome')

# how check os modules methods
print(dir(os))
print(len(dir(os)))

# Regular expression
import re
str = 'Hello Ben10'
y = re.findall('.',str)
print(y)
# * we can insert more metacharacters in this regular expression

# Regular expression methods - findall, serach, match, split, sub
txt = 'i am software engineering - supunsulak20@gmail'
y = re.findall('\w*a\w+',txt)
print(y)

y = re.search('software',txt)
print(y)

y = re.split('\s',txt)
print(y)

y = re.sub('\s','@',txt)
print(y)





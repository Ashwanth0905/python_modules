# -*- coding: utf-8 -*-
"""python_basics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tml11pA7jQZiGSK2U6ycAlb5TThz1_Xp

**What is python?**
1.Python is powerful programming language.

2.Specially used in data science,machine learning to solve daily life real-time problems and
providing the solutions.

3.Python is a high-level,intrepeted,interactive and object oriented scripting langauge.

**History of pyhton language**
1. Python was developed by "Guido Van Rossum" in late 1980's in National Research Institute
for Mathematics and Computer Science in Netherlands.

2. Python was derived from many other languages includingABC,Modulo-3,C,C++,Algol=68,SmallTalk,Unix shell and other scripting languages.

**Why python?**

1.Easy to understand

2.Easy syntax

3.Beginner friendly

4.Supports multiple libraries

5.Supports OOP's

**Applications of python**
1.Web applications

2.Desktop applications

3.Database applications

4.Web scraping

5.Wen mapping

6.Data analysis

7.Interactive web visualization

8.Computer vision and image processing etc.,
"""

import keyword
print(keyword.kwlist)
a=len(keyword.kwlist)
print(a)

"""**Indentation in python:**

1.In C,C++,the indentation is specified by using the flowerbrackdets{}.

2.In python,indentation is done by 4 white spaces or tab.

**Python comments:**

In python we have 2 types of comments such as follow:

1.single line comment(specified using single or double quotes)

2.multi line comment(specified using doc sring).
"""

#single line comment--->shows the single line comment.
print('hello my dear friends')

"""
multi line comment
how are you all
have a nice day guys
"""
print('hello CSE people')

"""**PYTHON VARIABLES:**

1.Variables are nothing but reserved memory locations to store values.

2.When we create a varaible ,automatically some space in memory isreserved.

3.Based on the data types the interpreter allocates the memory.

4.Varaible can take any data type such as integer,float numbers,strings etc.

"""

a=50
b=50
c=a+b
print(c)

"""**Python Data types**
1 integer data types
2 float point numbers
3 strings data type
4 boolean data type

**python data structures**
1.In python we have four types of data structures

2.These data structures are very useful and important while working with advance topics such
as machine learning ,data science.

1.List

2.Tuple

3.Dictionary

4.Sets

**1 lists in python**
List is a python data structure

it is a combination of any data type.

enclosed within [] and separated by commas(,).

list is sequence of values called items or elements.

list is similar arrays.

list mutable.

list is indexible.
"""

# creating a list with constructor()
a=([1,2,3,4,5])
b=([2,4,7,0,6,8])
c=(['hello','students'])
print(a)
print(b)
print(c)

type(a)

#creating ta list with heterogenous data:
a=(['hello',8,9,20.77])
print(a)

#creating a list with range function:
l=list(range(0,6))
print(l)

#creating a list without constructor():
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
print(days)

days[1]

#negative indexing:
#creating a list without constructor():
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
days[-1]

days[:]

days[1:4]

days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
days[1:4:2]

"""**list build-in function**"""

days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
len(days)

numbers=[1,2,3,4,5,6,7,8]
max(numbers)

numbers=[1,2,3,4,5,6,7,8]
min(numbers)

numbers=[1,2,3,4,5,6,7,8]
sum(numbers)

import random
numbers=[1,2,3,4,5,6,7,8]
random.shuffle(numbers)
print(numbers)

"""**list operator:**"""

a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

a=[10,20]
b=3*a
print(b)

days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
'wednesday' in days

ays=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
'wednesday'  not in days

a='Ashwanth'
b='Ashwanth'
a is b

a='Ashwanth'
b='Ashwath'
a is b

days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
del[days[1]]
days

a=['a','b','c','d']
print(a)
a.append('e')
print(a)

list=['red','orange','pink','black']
print(list)
list.clear()
print(list)

nums=[1,2,3,4,1,4,1,7,8,1]
print(nums)
nums.count(1)

list_1=[1,2,3,4]
print(list_1)
list_2=list_1.copy()
print(list_2)

A=[1,3,2,4,5]
B=[5,6,7,3,6]
print(A)
print(B)
A.extend(B)
print(A)

"""**python dict**"""

#create a dictionary
a={
'name':'joy',
'age':23,
'education':'Engineer'
}
print(a)

len(a)

type(a)

x=a.keys()
x

y=a.values()
y

z=a.items()
z

"""**Dict methods:**

**python sets**
"""

#Example:
set1={1,2,3,4}
print(set1)

#duplicates not allowed
set={1,2,3,4,5,6,7,1,1}
set

len(set)

type(set)

"""**python operators**

We have various python operators whcih are useful in performing various operat
Operators:

1.Arthematic operators

2.Comparison operators

3.Logical operators

4.Assignment operators

5.Special operators

a.Identity operators
b.Membership operators
"""

def add():
  a=2
  b=3
  sum=a+b
  return sum
add()
print(add())
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:53:13 2022

@author: Vincent Medrano
"""

statement = False
another_statement = True

if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

name = "Vincent"
age = 40
if name == "Vincent" and age == 40:
    print("Your name is Vincent, and you are also 40 years old.")

if name == "Vincent" or name == "Rick":
    print("Your name is either Vincent or Rick.")
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
    
# All conditions are True
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

# 16 is greater than 15
if number > 15:
    print("1")

# first_array contains numbers, True
if first_array:
    print("2")

# second_array does have 2 elements, True
if len(second_array) == 2:
    print("3")

# length of first_array is 3, second_array is 2 = 5, True
if len(first_array) + len(second_array) == 5:
    print("4")

#first_array and second_array first index is 1, True
if first_array and second_array[0] == 1:
    print("5")

#second_number is 0, if not 0, then True
if not second_number:
    print("6")
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:32:30 2022

@author: user
"""
# Exercise 1
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Exercise 2
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
       answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0! ")
    else:
        print(answer)

# Exercise 3
filename = 'alice.txt'

try:
    with open (filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry the file " + filename + " does not exist")
    
# Exercise 4
title = "Alice in Wonderland" 
print(title.split())

# Exercise 5 on Type error

print("Give me two numbers and I will add them together ")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number ")
    if first_number == "q":
        break
    second_number = input("Enter the second number ")
    
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print(" You can only add two numbers together ")
    else:
        print(str(answer))
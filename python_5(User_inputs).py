# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 07:17:10 2022

@author: user
"""

message = input("Tell me something and I will repeat it back to you: ")
print(message)


name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your name "

name = input(prompt)
print("Hello" + name + "!")


age = input("How old are you ")
age = int(age)
age >= 18

height = input("How tall are you in inches ? ")
height = int(height)

if height >= 36:
    print("\n You are tall enough to ride ")
else:
    print("\nYou will be able to ride when you are older ")

# Exercise 1: Check whether a number is odd or even 
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("The number " + str(number) + " is even")
else:
    print("The number " + str(number) + " is odd")
    
# Exercise 2: Checking cars during sales
info = {"Damilola": 20, "David": 25, "Isaiah": 26 
        }
info['Damilola'] += 2
print(info['Damilola'])

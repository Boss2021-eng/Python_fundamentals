# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 21:06:33 2022

@author: user
"""

# File Handling with files in the directory
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    
# File handling with reading from paths
with open('C:\\Users\\user\Desktop\\Desktop\\Python_Tutorials\\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    
# Reading line by line from a file 
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
# Making a list of lines from a file
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)
    for line in lines:
        print(line.rstrip())

# Working with a file contents 
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ' '
    for line in lines:
        pi_string += line.rstrip()
    print(pi_string)
    print(len(pi_string))
    
# WRITING TO A FILE
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love Programming')
    file_object.write('\nI love creating games')

# Appending texts to an already existing file
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write('I love finding meaning in large datasets. \n')
    file_object.write('I love creating games that run in a browser.\n')
    
# Exercise 1: Storing user's names as input in a file 

# Starting the file with the filename 'Names.txt'
filename = 'Names.txt'

# Accepting User's input
prompt = "Enter your name "
prompt += "\nEnter quit if you want to quit "
users = []

while True:
    user = input(prompt)
    if user.lower() == "quit" :
        break
    users.append(user)
        
print(users)  

with open(filename, 'w') as file_object:
    for user in users:
        file_object.write(user)
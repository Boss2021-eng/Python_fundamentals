# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:40:01 2022

@author: user
"""

# Storing objects in json files

import json

numbers = [2, 3, 5, 7, 11, 13]

# Storing files in a json file
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
    
# Retrieving files from a json file
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)    

# Storing Users input in a json file 
import json
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
print("We'll remember you when you come back, " + username + "!")

# Writing a problem that welcomes users whose data has been stored
import json 

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back " + username + "!")
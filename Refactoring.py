# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 07:32:41 2022

@author: user
"""

import json
def get_stored_username():
    """Get stored username if avaiable """
    filename = "üsername.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
    
def greet_user():
    """Greet users by name """
    username = get_stored_username()
    if username:
        print("Welcome back " + username + "!")
    else:
        username = input("What is your name? ")
        filename = "username.json"
        with open(filename, 'w') as f_obj:
           json.dump(username, f_obj)
        print("I will remember you when you come back " + username + "!")
    
greet_user()
        
# 10-11: Favorite number 
import json

def get_user_favoritenumber():
    """asks for user's favorite number and stores it """
    favorite_number = input("What is your favorite number? ")
    filename = "favorite_number.json"
    with open(filename, 'w') as f_obj:
        username = json.dump(favorite_number,f_obj)
    print("I know your favorite number! it is "  + favorite_number)

def favorite_number_remembered():
    """Retrieves user's favorite number if it is stored 
    and prompts the user for another if it is not """
    filename =  "favorite_number.json"
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        print(" I don't know your favorite number! ")
        print(" \nPlease enter your favorite number! ")
        favorite_number = input("What is your favorite number? ")
        filename = "favorite_number.json"
        with open(filename, 'w') as f_obj:
            username = json.dump(favorite_number,f_obj)
            print("I now know your favorite number! it is "  + favorite_number)
    else:
        print("I remember your favorite number!")
        print("Your favorite number is " + str(favorite_number))

get_user_favoritenumber()

favorite_number_remembered()   
    


# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 07:12:22 2022

@author: user
"""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")    
    
#function call
describe_pet('hamster','harry') #positional arguments (postion matters)
# keyword argument 
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name = 'bingo', animal_type = 'sheep dog')

# default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

describe_pet(pet_name='harry', animal_type='hamster')

# Exercise_1: Make shirt
def make_shirt(shirt_size,text_message):
    print(text_message + " should be printed on shirt of size " + shirt_size)
make_shirt("12 inches","Hello")

# Optional arguments
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Returning a dictionary
def build_person(first_name,last_name,age=''):
    """ Returns information about a person"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")  
    
    f_name = input('First name: ') 
    if f_name == 'q':
        break
    
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    
# Arbitary arguments
def build_profile(first,last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
 location='princeton',
 field='physics')
print(user_profile)
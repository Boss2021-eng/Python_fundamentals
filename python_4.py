# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 21:04:17 2022

@author: user
"""

# More on dictionary
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

alien_0['speed'] = 'fast'
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == "slow" :
    x_increment = 1
elif alien_0['speed'] == "medium":
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

alien_0['x_position'] = alien_0["x_position"] + x_increment
print("New x_postion: " + str(alien_0["x_position"]))

# Deleting key and value pairs from the dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del(alien_0['points'])

print(alien_0)

# A dictionary of similar objects
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# Exercise_1: Try it yourself
David = {'Name':'David', 'age':30, 'height': 'tall', 'skin':'dark'}
print(David['Name'])
print(David['age'])
print(David['height'])
print(David['skin'])

# Looping through a key_value pair in a dictionary
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key,Value in user_0.items():
    print("\nkey: " + key)
    print("\nValue: " + Value)
    
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is: " + language.title() + ".")
    
for name in favorite_languages.keys():
    print(name.title())

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + 
              ", I see your favorite language is "
              + favorite_languages[name].title() + '!')

for name in sorted(favorite_languages.keys()):
    print( name.title() + " ,thank you for taking the poll")
    
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language)
    
# Exercise_6.5: Rivers
rivers = {'Nigeria':'Niger','Egypt':'Nile', 'Anambra': 'River Anambra'}
for country,river in rivers.items():
    print("The river " + river + " runs across " + country + ".")
    
for country in rivers.keys():
    print(country)
    
for river in rivers.values():
    print(river)
    
# Nesting
# List of dictionaries 
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)


    
# Automatically generating aliens
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
    
# showing the first 5 aliens
for alien in aliens[:5]:
    print(alien)
    print('...')
    
# Showing how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))

# A list in a dictionary
# Store information about a pizza being ordered
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms','extra cheese']
    }

print("You have ordered a " + pizza['crust'] + " - crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
 
# A dictionary in a dictionary
users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

for username, user_info in users.items():
    print("\nusername: " + username)
    full_name = user_info['first'] + " " + user_info["last"]
    location = user_info["location"]
    print("full_name: " + full_name)
    print("location: " + location)
    
#Exercise: Talking about cities
cities = {
    'Lagos': {
    'country':'Nigeria',
    'population': '10,000,000',
    'fact': "It is Nigeria's most populous state"
    } ,
    'Washington DC': {
    'country':'USA',
    'population': '20,000,000',
    'fact': "It is USA's capital",   
        },
    'Kano': {
    'country': 'Nigeria',
    'population': '10,000,000',
    'fact': 'It is the northern part of Nigeria'
    }
    }
    
for city, city_info in cities.items():
    print(city)
    print("\n" + city_info['country'])
    print(city_info['population'])
    print(city_info['fact'])
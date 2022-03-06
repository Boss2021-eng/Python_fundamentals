# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 23:28:58 2022

@author: user
"""
# Strings
name = 'Ada Lovelace'
print(name.title())
print(name.lower())
print(name.upper())

first_name =  'Ada'
last_name = 'Lovelace'
full_name = first_name + " " + last_name
print(full_name)
print("Hello," + " " + full_name.title() + "!")

print("\tPython")
print("Languages:\nPython\nC\nJavascript")

# Sorting a list 
cars = ['bwm','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Sorting out a list temporarily
cars = ['bwm','audi','toyota','subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)


# Looping through a list 
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + ".\n")
print("Thank you, everyone. That was a great show!")

numbers = list(range(6))
print(numbers)

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Using if and conditional statements
cars = ['bwm','audi','toyota','subaru']
for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())
        
answer = 17
if answer != 17:
    print("That is not the correct answer. Please try again!")
    
age = 17

print(age < 21)

print(age <= 21)

print(age != 21)

print(age > 21)

print(age >= 21)

# Checking Multiple Conditions
# Using the if-elif-else condition
age = 12

if age < 4:
    print("Your admission rate is $0.")
elif age < 18:
    print("Your admission rate is $5.")
else:
    print("Your admission rate is $10.")
    


# A more concise way of writing the above 

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
    
print("Your admission ticket is $" + str(price) + ".")


# Exercise : Stages of life 

age = 12

if age < 2:
    person = "baby"
elif age > 2 and age < 4:
    person = "toddler"
elif age > 4 and age < 13:
    person = "kid"
elif age > 13 and age < 20:
    person = "teenager"
elif age > 20 and age < 65:
    person = "adult"
else:
    person = "elder"
    
print("The person is a " + str(person))

# Ordering pizzas_1
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
    
print("\nfinished making your pizzas")

# Ordering pizzas_2
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("sorry, we are out of green peppers for now")
    else:
        print("Adding " + requested_topping + ".")
    
print("\nfinished making your pizzas")

#Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, We don't have " + requested_topping + " right now.")
        
print("\nFinished making your pizza!")

# Exercise: Hello Admin
names = ["David","Segun","Stephen","Admin","Joshua"]
for name in names:
    if name == "Admin":
        print("Hello " + name + " would you like to see a status report?")
    else:
        print("Hello " + name + " thank you for logging in again")
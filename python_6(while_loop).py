# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 07:57:14 2022

@author: user
"""

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ''
while message.lower() != "quit":
    message = input(prompt)
    print(message)
    
#Using break statement
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    
    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title() + "!")
        
#Using continue
        
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
 
    print(current_number)
    
prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your name "

while True:
    name = input(prompt)
    print("Hello" + " " + name + " !")
    continue
# Exercise 1: Ordering for food
food_orders = ['rice','beans','plantain','eggs','meats']
finished_food = []

while food_orders:
    food = food_orders.pop()
    print("Adding " + food + ".")
    finished_food.append(food)
print("\ndisplaying the list of prepared food ")
for food in finished_food:
    print(food)
    
# Exercise 2: Removing repitive food 
food_orders = ['rice','beans','eggs','plantain','eggs','meats','eggs']

while 'eggs' in food_orders:
    food_orders.remove('eggs')
print("\nThe list of foods available")
for food in food_orders:
    print(food)

# Exercise 3: Removing repititive food
food_orders = ['rice','beans','eggs','plantain','eggs','meats','eggs']
food_orders = set(food_orders)

for food in food_orders:
    print(food)
    
# Exercise 4: Dream Vacation
prompt = "If you could visit one place in the world, where would you go? "

responses = {}
flag = True 

while flag:
    name = input("What is your name? ")
    response = input(prompt)

    # storing responses in a dictionary
    responses[name] = response
    
    # Find out if anyone wants to respond 
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        flag = False
    
    # Show the results
    print("\n--- PRINTING RESULTS ----")
    for name, response in responses.items():
        print(name + " would like to visit " + response + " on a dream vacation")

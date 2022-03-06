# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:02:11 2022

@author: user
"""

def make_pizza(size, *toppings):
 """Summarize the pizza we are about to make."""
 print("\nMaking a " + str(size) +
 "-inch pizza with the following toppings:")
 for topping in toppings:
     print("- " + topping)
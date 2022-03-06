# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 07:15:38 2022

@author: user
"""
import random
class Die():
    def __init__(self, sides = 6):
        """Initialize battery's attributes."""
        self.sides = sides
      
    
    def roll_die(self):
       """'roll die 10 times.""" 
       x = random.randint(1,6)
       print("Sides of Die: " + str(self.sides))
       print(x)
    
roll_1 = Die(20)
for i in range(10):
    roll_1.roll_die()
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 15:47:27 2022

@author: user
"""
# classes are capitalized 
class Dog(object):
    """ A simple attempt to model a dog """
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title()+ " is now sitting down.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
        
my_dog = Dog('wille',6)

print("My dog's name is " + my_dog.name.title() )
print("My dog is " + str(my_dog.age) + " years old!")

my_dog.sit()


        

user1 = User("Damilola","Olatayo", 35)
user1.describe_user()
user1.greet_user()
user1.login_attempts
user1.increment_login_attempts()
user1.reset_login_attempts()
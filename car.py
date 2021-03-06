# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 21:52:15 2022

@author: user
"""

class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
 
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
 
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
 
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
 
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        print("Odometer Reading: " + str(self.odometer_reading))
        
        
class Battery():
    def __init__(self, battery_size = 70):
        """Initialize battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing battery's size."""
        print("This Car has a " + str(self.battery_size) + " - KWh")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")       

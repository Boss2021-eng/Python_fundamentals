# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:35:31 2022

@author: user
"""

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
    
print(get_formatted_name('wolfgang','mozart','amadeus'))
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:36:22 2022

@author: user
"""

import unittest
from name_function import get_formatted_name

print(get_formatted_name('wolfgang','mozart','amadeus'))

class NameTestCase(unittest.TestCase):
     """Tests for name_function.py """
     
     def test_first_last_name(self):
         """ Do names like 'Janis Joplin' work ? """
         formatted_name = get_formatted_name('janis', 'joplin')
         self.assertEqual(formatted_name,"Janis Joplin")
         
     def test_first_last_middle_name(self):
        """ Do names like 'Wolfgang Amadeus Mozart' work ? """
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
        
unittest.main()
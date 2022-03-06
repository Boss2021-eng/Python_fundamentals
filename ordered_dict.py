# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 07:04:33 2022

@author: user
"""

from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

print(favorite_languages)

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
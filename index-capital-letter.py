# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:25:21 2021

@author: SONY
"""

a = list(input('write your word: '))
print([(index, item) for (index, item) in enumerate(list(a)) if 65<=ord(item)<=90])

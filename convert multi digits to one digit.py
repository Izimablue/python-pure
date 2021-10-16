# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:18:16 2021

@author: SONY
"""

x = int(input('Enter a number :'))
y = 0

while x > 0 :
    y += x % 10
    x = x // 10
    
    if x == 0 and y > 9 :
        x, y = y, x
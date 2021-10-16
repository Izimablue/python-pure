# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:40:06 2021

@author: SONY
"""

def double_letters(a:str) -> bool:
    for i in range(len(a)):
        print('\n', i)
        if i == len(a)-1:
            return 'false'
        elif list(a)[i] == list(a)[i+1]:
            return 'true'

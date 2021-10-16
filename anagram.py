# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:49:52 2021

@author: SONY
"""

def is_anagram(a:str, b:str) -> bool:
    a = list(a)
    b = list(b)
    if len(a) == len(b):
        for i in a:
            if i in b:
                b.remove(i)
        if b == []:
            return bool(1)
        else:
            return bool(0)
    else:
        raise ValueError('The length of two words should be equal')
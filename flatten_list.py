# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 18:00:51 2021

@author: SONY
"""

def flatten(a:list) -> list:
    if not isinstance(a, list):
        raise TypeError("input must be of a list type")
    for (index, i) in enumerate(a):
        if type(i) == list:
            if bool(i)==False:
                a.remove(i)
            for (jindex, j) in enumerate(i):
                while bool(i)==True:
                    a.insert(index, i.pop())
    return a
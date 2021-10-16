# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:09:30 2021

@author: SONY
"""

def count_sylabels(a:str) -> int:
    i1 = 0
    for i in range(len(a)):
        if i < len(a) and list(a)[i] == '-':
            i1 = i1 + 1
    return i1+1
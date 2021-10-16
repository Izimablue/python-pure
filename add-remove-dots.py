# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:05:26 2021

@author: SONY
"""

def add_dots(a:str) -> str:
    l1 = []
    for i in range(len(a)):
        if i < len(a)-1:
            l1.extend([list(a)[i], '.'])
        else:
            l1.append(list(a)[i])
    return ''.join(l1)
    
    
def remove_dots(a:str) -> str:
    l2 = []
    l2 = list(a)
    for i in a:
        if i == '.':
           l2.remove(i)
    return ''.join(l2)

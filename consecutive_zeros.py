# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:53:19 2021

@author: SONY
"""

def consecutive_zeros(a:str) -> int:
    l = [[]]
    for i in a:
        if i == "0":
            l[-1].append(i)
        else:
            l.append([])
    return max(map(lambda a: len(a), l))
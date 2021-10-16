# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:14:33 2021

@author: SONY
"""

def tiktaktoe(a:str) -> list:
    dic = {'A':0, 'B':1, 'C':2}
    return (int(list(a)[1])-1, dic[list(a)[0]])
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:51:26 2021

@author: SONY
"""
# import cPickle as pickle

def mid(a: str) -> str:
    if not isinstance(a, str):
        raise TypeError('input is not of type string')
    if list(a).index(list(a)[-1]) % 2 == 1:
        return ("")
    else :
        return list(a)[int((list(a).index(list(a)[-1]))/2)]
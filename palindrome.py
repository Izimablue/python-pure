# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:35:38 2021

@author: SONY
"""

def palindrome(a:str) -> str:
    b = "".join(list(a)[::-1])
    if a == b:
        return bool(1)
    else:
        return bool(0)
    
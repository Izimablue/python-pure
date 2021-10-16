# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:08:10 2021

@author: SONY
"""

def all_equal(a:list) -> bool:
    for i in a:
        while a:
            if a[0] != a.pop():
                return bool(0)
            elif len(a) == 0:
                return bool(1)
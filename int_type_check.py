# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:38:32 2021

@author: SONY
"""

def only_ints(a:int, b:int) -> bool:
    if isinstance(a, int) & isinstance(b, int):
        return 'true'
    else:
        return 'false'
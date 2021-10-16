# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:36:44 2021

@author: SONY
"""

def list_xor(a, l1, l2):
    print(bool(0) if a in l1 and a in l2 else bool(1) if a in l1 or a in l2 else bool(0))
    
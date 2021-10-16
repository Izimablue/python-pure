# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:27:34 2021

@author: SONY
"""

def zap(a, b):
    l = []
    for i in range(len(a)):
        l.append((a[i], b[i]))
    return l
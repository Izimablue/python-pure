# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:15:29 2021

@author: SONY
"""

import time
from functools import wraps

def time_of_execution(func):
    ### calculating execution time of any arbitary operation ###
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_s = time.time()
        result = func(*args, **kwargs)
        t_e = time.time()
        return result
    return wrapper


@time_of_execution
v = int(input('Specify your volume: '))
a = set()
b = []
for x in range(1, v+1):
    for y in range(x, v+1):
        for z in range(y, v+1):
            if x*y*z == v:
                a.add(2*(x*y + x*z + y*z))
                b.append(2*(x*y + x*z + y*z))
print(min(a))
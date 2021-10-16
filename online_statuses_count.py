# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:24:30 2021

@author: SONY
"""

def oncount(user_count):
    user_stat = {}
    for i in range(user_count):
        print("user:", i+1)
        user_name = str(input("insert user's name: "))
        user_status = str(input("insert user's status: "))
        user_stat[user_name] = user_status
    j = 0
    for x, y in user_stat.items():
        if y == 'online':
            j+=1
    print(j)
    
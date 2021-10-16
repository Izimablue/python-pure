# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:35:36 2021

@author: SONY
"""


def format1(number):
    nl = list(str(number))
    if len(nl) > 3:
        if len(nl) % 3 != 0:
            for i in range(len(nl)//3):
                nl.insert((-3-4 * i), ",")
        else:
            for i in range((len(nl)//3)-1):
                nl.insert((-3-4 * i), ",")
        return "".join(nl)
    else:
        return str(number)


def format(number):
    nl = list(str(number))
    a = []
    fa = []
    # if len(nl)
    for i in range(len(str(number))//3):
        # print('here')
        a.append([',', nl[-3:]])
        # print('a: ', a)
        nl = nl[:-3]
        # print('nl: ', nl)
    a = [a.pop() for i in range(len(a))]
    # print('a: ', a)
    for i in a:
        for j in i:
            for k in j:
                fa.append(k)
    # print('fa: ', fa)
    while nl:
        fa.insert(0, nl[-1])
        nl.pop()
    # print('fa: ', fa)
    if fa[0] == ',':
        fa = fa[1:]
    return (''.join(fa))

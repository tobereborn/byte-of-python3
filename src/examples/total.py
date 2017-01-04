#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 4, 2017

@author: weizhenjin
'''

def total(initial=5, *numbers, **keywords):
    cnt = initial
    for number in numbers:
        cnt += number
    for key in keywords:
        cnt += keywords[key]
    return cnt;

print(total(10, 1, 2, 3, vegetables=50, fruits=100))

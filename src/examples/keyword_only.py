#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 4, 2017

@author: weizhenjin
'''

def total(initial=5, *numbers, vegetables):
    cnt = initial
    for number in numbers:
        cnt += number
    cnt += vegetables
    return cnt;

print(total(10, 1, 2, 3, vegetables=50))

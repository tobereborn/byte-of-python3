#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 5, 2017

@author: weizhenjin
'''

def get_error_details():
    return (2, 'second error details')

errnum, errstr = get_error_details()

print(errnum)
print(errstr)

a, *b = [1, 2, 3, 4]
print(a)
print(b)

a = 5
b = 8

a, b = b, a

print(a)
print(b)

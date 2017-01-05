#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast
    
try:
    s = input('Enter something -->')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
        
except EOFError:
    print('Why did you do an EOF on me>')
except ShortInputException as ex:
    print('The input was of lenght {0},it should be at least {1}'.format(ex.length, ex.atleast))
else:
    print('No exception was raised.')
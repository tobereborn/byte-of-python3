#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

try:
    text = input('Enter something -->')
except EOFError:
    print('\nWhy did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation')
else:
    print('You enter:{0}'.format(text))
    
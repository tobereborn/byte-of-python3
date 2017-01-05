#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 5, 2017

@author: weizhenjin
'''

with open('poem.txt') as f:
    for line in f:
        print(line, end='')
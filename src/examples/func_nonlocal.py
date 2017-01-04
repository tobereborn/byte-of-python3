#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 4, 2017

@author: weizhenjin
'''

def func_outer():
    x = 2
    print('X is', x)
    
    def func_inner():
        nonlocal x
        x = 5
    
    func_inner()
    print('Change x to', x)

func_outer()

        
        

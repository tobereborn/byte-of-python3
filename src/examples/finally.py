#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

import time

try:
    f = open('poem.txt')
    while True:
        l = f.readline()
        if len(l) == 0:
            break
        print(l, end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('You cancelled the reading from file')
finally:
    print('Cleaning up...')
    f.close()

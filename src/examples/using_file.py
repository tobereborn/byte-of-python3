#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

poem = '''\
Programming is fun
When the work is done
if (you wanna make your work also fun):
use Python!
'''

f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:  # EOF
        break
    print(line, end=' '),  # So that extra newline is not added
f.close()

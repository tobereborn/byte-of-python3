#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print (storedlist)

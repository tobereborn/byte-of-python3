#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 4, 2017

@author: weizhenjin
'''

bri = set(['brazil', 'russia', 'india'])
print ('india' in bri)
print ('usa' in bri)
bric = bri.copy()
bric.add('china')
print(bric.issubset(bri))
bri.remove('russia')
print(bri & bric)

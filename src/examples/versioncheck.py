#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 5, 2017

@author: weizhenjin
'''

import sys, warnings

if sys.version_info[0] < 3:
    warnings.warn('Need python 3 to run', RuntimeWarning)
else:
    print('Proceed as normal')
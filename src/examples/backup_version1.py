#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

import os
import time

source = ['~/TbrGitHub/tmp/t1', '~/TbrGitHub/tmp/f3']
target_dir = '~/TbrGitHub/tmp/backup'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}" .format(target, ' '.join(source))

print (zip_command)

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

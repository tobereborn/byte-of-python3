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

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%s')

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

target = today + os.sep + now + '.zip'

zip_command = "zip -qr {0} {1}" .format(target, ' '.join(source))

print(zip_command)

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

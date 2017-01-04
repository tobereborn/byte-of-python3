#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Dec 31, 2016

@author: weizhen
'''

ab = {'Swaroop':'python@g2swaroop.net',
      'Miguel' : 'miguel@novell.com',
      'Larry' : 'larry@wall.org',
      'Spammer' : 'spammer@hotmail.com'
    }

print ("Swaroop's address is", ab['Swaroop'])

ab['Guido'] = 'guido@python.org'
del ab['Spammer']

print ('\nThere are {0} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))
    
if 'Guido' in ab:
    print("\nGuido's address is" , ab['Guido'])

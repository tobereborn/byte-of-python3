#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ('(Initialized SchooolMember:${0})'.format(self.name))
    
    def tell(self):
        print('Name: {0} Age: ${1:d}'.format(self.name, self.age), end='')
           
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: ${0})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Salary:${0:d}'.format(self.salary))
    
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: ${0})' .format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: ${0:d}' .format(self.marks))
    
t = Teacher('Mrs.Abraham', 40, 30000)
s = Student('Swaroop', 21, 75)

print()

members = [t, s]
for member in members:
    member.tell()

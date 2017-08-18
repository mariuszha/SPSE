#!/usr/bin/env python

# class.py by mariuszha
#
# Purpose:
# Simple code defining class and inheritance 
#


class Calculator:

	def __init__(self, ina, inb):
		self.a = ina
		self.b = inb

	def add(self):
		return self.a + self.b

	def mul(self):
		return self.a*self.b



class Scientific(Calculator):

	def power(self):
		return pow(self.a,self.b)


first_num = int(raw_input('Write a first number: '))
second_num = int(raw_input('Write a second number: '))

newCalculation = Calculator(first_num, second_num)

print 'a+b: %d' % newCalculation.add()

print 'a*b: %d' % newCalculation.mul()


third_num = int(raw_input('Write a third number: '))
forth_num = int(raw_input('Write a forth number: '))

newPower = Scientific(third_num, forth_num)

print 'c+d: %d' % newPower.add()

print 'c*d: %d' % newPower.mul()

print 'c pow d: %d' % newPower.power()

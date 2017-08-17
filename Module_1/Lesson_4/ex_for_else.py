#!/usr/bin/python

# ex_for_else.py by mariuszha
#
# Excercise:
# For loop with else 
#

fruits = ["apple", "bannana", "orange"]

input = raw_input("What fruit you are looking for? ")
for fruit in fruits:
	if fruit == input:
		print fruit
		break
else:
	print "There is no %s here" % (input)
  

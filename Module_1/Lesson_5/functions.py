#!/usr/bin/python2.7

# functions.py by mariuszha
# 
# purpose:
# Create funcions on your own
#
# This funciton search for 'a' in a given string
#
# Usage: ./funcions.py 'searched string'

import sys

def find_a_in_a_string(searched_string):

	counter = 0
	for character in searched_string:
		if character == 'a':
			counter = counter + 1
		else:
			continue
	print("There are %s letters 'a' in a string." % counter)

find_a_in_a_string(sys.argv[1])

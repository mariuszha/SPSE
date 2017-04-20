#!/usr/bin/python2.7

#
# ex.fnmatch.py v1.0 by mariuszha
#

import os
import fnmatch

for item in os.listdir('.'):
	if fnmatch.fnmatch(item, '*'):
		print item

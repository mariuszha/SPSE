#!/usr/bin/python2.7

# ex.recur.list.dir.py v1.0 by mariuszha
# 
# Excercise:
# List recurcively all files in a current directory and in subdirectories
#

import os
from fnmatch import fnmatch

root = os.getcwd()
pattern = "*"

for path, subdir, files in os.walk(root):
	for name in files:
		if fnmatch(name, pattern):
			print os.path.join(path, name)
      

#!/usr/bin/python2.7

# 
# ex.stat.file.py v1.0 by mariuszha
#

import os
import datetime
import sys
from stat import *

top = os.getcwd()

for f in os.listdir(top):
	pathname = os.path.join(top, f)
	mode_uid = os.stat(pathname).st_uid
	mode_gid = os.stat(pathname).st_gid
	mode_size = os.stat(pathname).st_size
	mode_atime = os.stat(pathname).st_atime
	mode_mtime = os.stat(pathname).st_mtime
	print 'Path: %s' % pathname
	print 'UID: %s' %  mode_uid
	print 'GID: %s' % mode_gid
	print 'SIZE: %s' % mode_size
	print 'Access time: %s' % datetime.datetime.fromtimestamp(mode_atime)
	print 'Modification time: %s' % datetime.datetime.fromtimestamp(mode_mtime) 

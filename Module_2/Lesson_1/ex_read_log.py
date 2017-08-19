#!/usr/bin/env python

# ex_read_log.py by mariuszha
#
# Purpose:
# Find all the logs in the /var/log/syslog which pertain to CMD
# and print them out selectively 
#


with open("/var/log/syslog") as f:
	for line in f:
		if "CMD" in line:
			print line
 

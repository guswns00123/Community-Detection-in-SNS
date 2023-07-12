#!/usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	followee, follower = line.split(' ')
	print("%s\t%s" %(follower, followee))
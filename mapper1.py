#!/usr/bin/env python
import sys


for line in sys.stdin:
    line = line.strip()
    cur_followee, follower = line.split(' ')
    print("%s\t%s" % (cur_followee, follower))


#!/usr/bin/env python

import sys


for line in sys.stdin:
    line = line.strip()
    pair1, followee, cnt = line.split('\t')
    id = pair1.split(":")[0]
    if id[-3:] == "531":
        print("%s, {%s}, %s" % (pair1, followee, cnt))
    
#!/usr/bin/env python

import sys


for line in sys.stdin:
    line = line.strip()
    pair1, pair2, followee, cnt = line.split('\t')
    p1 = int(pair1)
    p2 = int(pair2)
    print("%d\t%d\t%s\t%s" % (p1, p2, followee, cnt))
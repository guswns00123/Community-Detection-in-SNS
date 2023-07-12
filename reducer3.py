#!/usr/bin/env python
import sys
last_pair = None
max_followee_list = None
max_pair1 = None
max_pair2 = None
max = 0
for line in sys.stdin:
    line = line.strip()
    pair1, pair2, followee, cnt = line.split('\t')
    pair = pair1 + ":" + pair2
    if pair1 == last_pair:
        if cnt > max:
            max = cnt
            max_pair1 = pair
            max_followee_list = followee[:]
        elif cnt == max:
            max = cnt
            if max_pair2 < pair2:
                max_pair1 = pair
                max_followee_list = followee[:]
    else:
        if last_pair is not None:
            print("%s\t%s\t%s" % (max_pair1, max_followee_list, max))
            max = cnt
            max_followee_list = followee[:]
            max_pair1 = pair
            last_pair = pair1
            max_pair2 = pair2
        elif last_pair is None:
            max = cnt
            max_followee_list = followee[:]
            max_pair1 = pair
            last_pair = pair1
            max_pair2 = pair2

print("%s\t%s\t%s" % (max_pair1, max_followee_list, max))
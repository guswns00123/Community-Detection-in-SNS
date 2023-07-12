#!/usr/bin/env python

import sys

last_pair = None
followee_list = []

for line in sys.stdin:
    line = line.strip()
    pair1, pair2, followee = line.split('\t')
    pair = pair1 + ":" + pair2
    if pair == last_pair:
        followee_list.append(followee)
    else:
        if last_pair is not None:
            print("%s\t%s\t%s\t%d" % (pair1, pair2, followee_list, len(followee_list)))
            followee_list = []
            last_pair = pair
            followee_list.append(followee)
        elif last_pair is None:
            followee_list.append(followee)
            last_pair = pair

print("%s\t%s\t%s\t%d" %(pair1, pair2, followee_list, len(followee_list)))
#!/usr/bin/env python
import sys

last_follower = None
followee_list = []

for line in sys.stdin:
    line = line.strip()
    cur_follower, followee = line.split('\t')
    if cur_follower == last_follower:
        followee_list.append(followee)
    else:
        if last_follower is not None:
            print("%s\t%s" % (last_follower, followee_list))
            followee_list = []
            last_follower = cur_follower
            followee_list.append(followee)
        elif last_follower is None:
            followee_list.append(followee)
            last_follower = cur_follower

print("%s\t%s" % (last_follower, followee_list))

#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    cur_followee, follower_list = line.split('\t')
    follower_list = follower_list[1:-1].split(',')
    for i in follower_list:
        for j in follower_list:
            if i != j:
                pair1 = i.strip()
                pair2 = j.strip()
                p1 = int(pair1[1:len(pair1)-1])
                p2 = int(pair2[1:len(pair2)-1])
                print("%d\t%d\t%s" % (p1, p2, cur_followee))

                

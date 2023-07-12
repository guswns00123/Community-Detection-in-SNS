#!/usr/bin/env python
from operator import itemgetter
import sys

last_followee = None
follower_list = []

for line in sys.stdin:
    line = line.strip()
    cur_followee, follower = line.split('\t')
    
    
    if cur_followee == last_followee:
        follower_list.append(follower)
    else:
        if last_followee is not None:
            follower_list.sort()
            print("%s\t%s" % (last_followee, follower_list))
            follower_list = []
            last_followee = cur_followee
            follower_list.append(follower)
        elif last_followee is None:
            follower_list.append(follower)
            last_followee = cur_followee

print("%s\t%s" %(last_followee, follower_list))



# for line in sys.stdin:
#     line = line.strip()
#     cur_followee, follower_list = line.split('\t')
#     follower_list = follower_list[1:-1].split(',')
#     for i in follower_list:
#         for j in follower_list:
#             if i != j:
#                 pair = i.strip() + ":" + j.strip()
#                 print("%s\t%s" % (cur_followee, pair))



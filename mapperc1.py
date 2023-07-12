#!/usr/bin/env python
import sys
import ast

check = ""

community_list = {} # to save community info
#./hw1/small/small_label
with open('medium_label') as f:
	for line in f.readlines():
		community = line.strip()
		blog_id, community = community.split(' ')
		community_list.update({blog_id: community})

for line in sys.stdin:
    line = line.strip()
    followee, follower_list = line.split('\t')
    follower_list = ast.literal_eval(follower_list)
    community = community_list[followee]
    if len(follower_list) > 1:
        check = "o"
    else:
        check = "x"
    print("%s\t%s\t%s" % (community, followee, check))



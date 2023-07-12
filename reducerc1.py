#!/usr/bin/env python
import sys

last_commu = None
followee_list = {}
cnt = 0

for line in sys.stdin:
    line = line.strip()
    cur_commu, followee, check = line.split('\t')
    # print("%s\t%s\t%s" % (cur_commu, followee, check))
    if cur_commu == last_commu:
        followee_list[followee] = check
        if check == 'o':
            cnt += 1
    else:
        if last_commu is not None:
            print("Community %s:\t%s" % (last_commu, cnt))
            cnt = 0
            followee_list = {}
            last_commu = cur_commu
            followee_list[followee] = check
            if check == 'o':
                cnt += 1
        elif last_commu is None:
            followee_list[followee] = check
            if check == 'o':
                cnt += 1
            last_commu = cur_commu

print("Community %s:\t%s" % (last_commu, cnt))
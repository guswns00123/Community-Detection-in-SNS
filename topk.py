#!/usr/bin/env python
import sys
import ast

last_pair = None
cnt = 0
for line in sys.stdin:
    line = line.strip()
    pair1, sim,  pair2, followee_list   = line.split('\t')
    followee_list = ast.literal_eval(followee_list)
    if pair1 == last_pair:
        if cnt < 3:
            if pair1[-3:] =="531":
                print("%s:%s, {%s}, %s" % (pair1, pair2, followee_list, sim))
            cnt += 1
    else:
        if last_pair is not None:
            cnt = 0
            if pair1[-3:] =="531":
                print("%s:%s, {%s}, %s" % (pair1, pair2, followee_list, sim))
            last_pair = pair1
            cnt += 1

        elif last_pair is None:
            if pair1[-3:] =="531":
                print("%s:%s, {%s}, %s" % (pair1, pair2, followee_list, sim))
            last_pair = pair1
            cnt += 1
            


#!/usr/bin/env python
import sys
import ast

dictionary = {}

for line in sys.stdin:
    line = line.strip()
    follower, followee_list = line.split('\t')
    followee_list = ast.literal_eval(followee_list)
    dictionary[follower] = followee_list


for k in dictionary:
    for j in dictionary:
        if k != j:
            if len(dictionary[k]) == 0 or len(dictionary[j]) == 0:
                continue
            else:
                common = list(set(dictionary[k]) & set(dictionary[j]))
                len_c = len(common)
                total = len(list(set(dictionary[k]) | set(dictionary[j])))
                print("%s\t%s\t%s\t%d\t%d" % (k, j, common, len_c, total))



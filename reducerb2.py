#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    pair1, pair2, common_list, len_c, total = line.split('\t')
    similarity = float(len_c) / float(total)
    if similarity > 0:
        print("%s\t%s\t%s\t%s" % (pair1, similarity, pair2, common_list))
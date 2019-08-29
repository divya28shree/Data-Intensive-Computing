#!/usr/bin/env python

from operator import itemgetter
import sys

a = None
b = 0
pair = None

for line in sys.stdin:
    line = line.strip()
    pair, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue

    if a == pair:
        b += count
    else:
        if a:
            print('%s\t%s' % (a, b))
        b = count
        a = pair

if a == pair:
    print('%s\t%s' % (a, b))

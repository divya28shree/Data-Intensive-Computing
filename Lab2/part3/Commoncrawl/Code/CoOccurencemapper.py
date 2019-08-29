#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
import sys

top10 = ['said','new','one','like','art','work','also','year','film','time']

window = 2

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    i = 0
    while i <len(words):
        j = 0
        while j <len(words):
            if i!= j:
            	if words[i] in top10 or words[j] in top10:
                	print("%s%s\t%d" % (words[i]+' ', words[j], 1))
            j+=1
        i+=1
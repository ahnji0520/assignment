#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

###############################################################################
def word_count(filename):
    """ 단어 빈도 dictionary를 생성한다. (key: word, value: frequency)
    
    filename: input file
    return value: a sorted list of tuple (word, frequency) 
    """
    ahn = open(filename, encoding = 'UTF8')
    
    d = {}
    
    for line in ahn.readlines():
        word = line.strip()
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    p = sorted(d.items())
        
    return p

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    result = word_count(sys.argv[1])

    # list of tuples
    for w, freq in result:
        print( "%s\t%d" %(w, freq))

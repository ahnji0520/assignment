#!/usr/bin/env python3
# coding: utf-8

import sys

def get_morphs_tags(tagged):

    result = []

    x = tagged.split('+')

    for i in x:
        if i == '':
            idx = x.index('')
            del x[idx]
            x[idx] = '+' + x[idx]

    for i in x:
        y = i.split('/')
        if '' in y:
            del y[0]
            y[0] = '/'
        p = tuple(y)
        result.append(p)

    return result

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1]) as fin:

        for line in fin.readlines():

            # 2 column format
            segments = line.split('\t')

            if len(segments) < 2: 
                continue

            # result : list of tuples (morpheme, tag)
            # "결과/NNG+는/JX" : [('결과', 'NNG'), ('는', 'JX')]
            result = get_morphs_tags(segments[1].rstrip())
        
            for morph, tag in result:
                print(morph, tag, sep='\t')

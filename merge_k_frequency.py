#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 복수의 빈도 파일을 병합하는 프로그램

import sys
import heapq

###############################################################################
def merge_k_sorted_freq(input_files):
    '''
    input_files : list of input filenames (frequency files; 2 column format)
    '''
    fins = [] # list of file objects
    k = len(input_files)
    heap = []
    finished = [False for _ in range(k)] # [False] * k
    
    for i in range(k):
        fins.append(open(input_files[i]))
    
    for i in range(k):
        line = fins[i].readline()
        word = line.split('\t')
        word.append(i)
        heapq.heappush(heap, word)
    
    a = heapq.heappop(heap)
    b = [a[0], a[1]]
    b[1] = int(b[1])
    
    line = fins[a[2]].readline()
    word = line.split('\t')
    word.append(a[2])
    heapq.heappush(heap, word)

    while heap != []:
        
        a = heapq.heappop(heap)

        if a[0] == b[0]:
            c = int(a[1])
            b[1] += c
            if heap == []:
                print(b[0], b[1], sep='\t') 

        else:
            print(b[0], b[1], sep='\t')
            b = a
            b[1] = int(b[1])

        line = fins[a[2]].readline()

        if line:
            word = line.split('\t')
            word.append(a[2])
            heapq.heappush(heap, word)

        else:
            finished[a[2]] = True    
              
    for i in range(k):
        fins[i].close()

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    merge_k_sorted_freq( sys.argv[1:])

#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    st1_th, st2_th, st3_th = 0, 0, 0
    
    for i in h1:
        st1_th += i
    for i in h2:
        st2_th += i
    for i in h3:
        st3_th += i
    while st1_th !=0 and st2_th != 0 and st3_th != 0 and (st1_th!=st2_th or st2_th!=st3_th):
        if max(st1_th, st2_th, st3_th) == st1_th:
            st1_th = st1_th - h1[0]
            h1.pop(0)
        elif max(st1_th, st2_th, st3_th) == st2_th:
            st2_th = st2_th - h2[0]
            h2.pop(0)
        else:
            st3_th = st3_th - h3[0]
            h3.pop(0)
    else:
        if st1_th==st2_th and st2_th==st3_th:
            return st1_th
        else:
            return 0

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

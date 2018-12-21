#!/bin/python3

import math
import os
import random
import re
import sys

def bitwise(n,k):
    if k % 2 == 1:
        return(k - 1)
    elif math.log(k, 2).is_integer():
        if n >= k*2-1:
            return(k - 1)
        else:
            return(k - 2)
    else:
        if n >= (k&(k-1))+(k^(k-1)):
            return(k - 1)
        else:
            return(k - 2)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(bitwise(n,k))

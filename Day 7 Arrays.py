#!/bin/python3

import math
import os
import random
import re
import sys

def out(arr):
    a= str(arr[-1])
    size = len(arr)

    for i in range(size-2,-1,-1):
        a += str(' '+str(arr[i]))

    print(a)
    return

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

out(arr)

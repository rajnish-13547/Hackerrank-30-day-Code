#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(arr):
    val = -10000
    x = len(arr)
    y = len(arr[0])

    for i in range(x-2):
        val_v = 0
        for j in range(y-2):
            val_v = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+2][j+2]+arr[i+1][j+1]+arr[i+2][j+1]+arr[i+2][j]

            if val_v>val:
                val = val_v
    return val


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

print(hourglass(arr))

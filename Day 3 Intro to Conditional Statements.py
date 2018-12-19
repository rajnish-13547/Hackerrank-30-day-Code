#!/bin/python3

import math
import os
import random
import re
import sys

def con(n):
    if n%2:
        return print('Weird')
    else:
        if 2<=n<6:
            return print('Not Weird')
        elif n<21:
            return print('Weird')
        else:
            return print('Not Weird')

if __name__ == '__main__':
    N = int(input())

con(N)

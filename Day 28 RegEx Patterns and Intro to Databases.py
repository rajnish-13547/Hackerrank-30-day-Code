#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    out = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        out1 = re.compile('^[a-z^\.]*'+firstName+'@gmail.com').findall(emailID)
        if out1: out.append(firstName)

    for val in sorted(out): print(val)

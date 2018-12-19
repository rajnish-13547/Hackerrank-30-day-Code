#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    out = bin(n)[2:].split('0') #bin binarizes into form '0b----' where ---- is binary representataion

    out = len(max(out)) # choosing maximum length of string as '11' > '1'
    print(out)

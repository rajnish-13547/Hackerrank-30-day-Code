#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
total =0
for i in range(n):
    swap = 0
    for j in range(n-1):
        if a[j]>a[j+1]:
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp
            swap +=1
            total += 1

    if swap == 0: # Nothing left to swap
        break

print("Array is sorted in",total,'swaps.')
print('First Element:',a[0])
print('Last Element:',a[-1])

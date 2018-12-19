# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def is_prime(val): #O(sqrt(n)) algorithm
    if val==1:
        return 'Not prime'
    elif val ==2 or val == 3:
        return 'Prime'
    else:
        for i in range(2,int(math.sqrt(val))+1,1): # for a*b=n and a<b: possible max(a) = sqrt(n) = min(b)
            if val%i ==0:
                return 'Not prime'

        return 'Prime'

t = int(input())
for i in range(t):
    print(is_prime(int(input())))

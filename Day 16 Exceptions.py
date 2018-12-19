import sys
S = input().strip()
try:
    s = int(S)
    print(s)
except Exception:
    print('Bad String')

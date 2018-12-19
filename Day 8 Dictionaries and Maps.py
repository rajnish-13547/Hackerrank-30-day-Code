# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phones = {}
for i in range(n):
    k,v = str(input()).split(' ')
    phones[k]=v

for j in range(0,n):
    query = input()
    if query in phones.keys():
        print(str(query)+'='+str(phones[query]))
    else:
        print('Not found')

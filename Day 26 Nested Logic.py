# Enter your code here. Read input from STDIN. Print output to STDOUT
final = list(map(int,input().rstrip().split()))
end = list(map(int,input().rstrip().split()))


def fine(final,end):
    if (final[-1]-end[-1])>0: return int(10000)
    if (final[-1]-end[-1])<0: return 0
    elif (final[-2]-end[-2])>0: return int(500*(final[-2]-end[-2]))
    elif (final[0]-end[0])>0: return int(15*(final[0]-end[0]))
    else: return 0

print(fine(final,end))

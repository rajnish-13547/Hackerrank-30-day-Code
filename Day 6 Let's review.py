# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

def half_string(word):
    size = len(word)
    out1 = word[0]
    out2 = word[1]

    for i in range(2,size):
        if i%2:
            out2 += str(word[i])
        else:
            out1 += str(word[i])

    print(out1,out2)
    return


for i in range(n):
    string = str(input())
    half_string(string)

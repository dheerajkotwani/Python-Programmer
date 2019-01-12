from operator import xor
a=int(input())
for i in range(a):
    b, c=map(int,input().split())
    print(b)
    print(c)
    for j in range(b+1,c+1):
        b=xor(b,i)

    if b%2==0:
        print("Even")
    else:
        print("Odd")

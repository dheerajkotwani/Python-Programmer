n=int(input())
for i in range(n):
    s=0
    m=int(input())
    for i in range(1,m):
        if m%i==0:
            s+=i
    print(s)

n=int(input())
for i in range(n):
    m=int(input())
    s=0
    for j in range(1,m+1):
        if m%j==0:
            s+=1
    print(s)

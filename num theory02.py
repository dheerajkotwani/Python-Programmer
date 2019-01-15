n, x=map(int,input().split())
b=list(map(int,input().split()))
s=x
m=0
for i in b:
    s=s-i
    m=m+1
    
    if s<=0:
        print(m)
        exit()

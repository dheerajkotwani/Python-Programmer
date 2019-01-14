n=int(input())
b=map(int,input().split())
c=int(input())
s=-1
for i in b:
    s+=1
    if i==c:
        print(s)
        exit()

n=int(input())
s=0
for i in range(n):
    a, b=map(int,input().split())
    if a/b>=1.6 and a/b<=1.7 or b/a>=1.6 and b/a<=1.7:
        s+=1
print(s)

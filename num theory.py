from array import *
arr=array('i',[])
n=int(input())
for i in range(n):
    x=int(input())
    arr.append(x)
k=min(arr)
for i in range(2,k):
    a=arr[0]%i
    s=0
    for j in arr:
        if j%i==a:
            s+=1
    if s==len(arr):
        print(i,end=" ")

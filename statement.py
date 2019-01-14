s=['A','E','I','O','U','a','e','i','o','u']
n=int(input())
for i in range(n):
    sum=0
    arr=input()
    for j in arr:
        if j in s:
            sum+=1
    print(sum)

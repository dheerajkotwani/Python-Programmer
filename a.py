n=int(input())
for j in range(n):
    s=0
    a=input()
    b=input()
    a=sorted(a)
    b=sorted(b)
    for i in a:
        if i not in b:
            s+=1
    for i in b:
        if i not in a:
            s+=1
    print(s)

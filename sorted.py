n = int(input())
for i in range(n):
    a, b =input(), input()
    if (sorted(a) == sorted(b)):
        print("YES")
    else:
        print("NO")


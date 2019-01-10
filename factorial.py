num=int(input("Enter a number"))
f=1
def fact(n):
    global f
    if(n!=1):
        f=n*fact(n-1)
    else:
        return 1
    return f
fact(num)
print("Factorial of ",num," is", f)

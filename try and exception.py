a=10
b= int(input("Enter a number"))


try:
    print("Resource Open")
    print("a/b=", a/b)
except Exception as e:
    print("You Cannot divide a number by Zero", e)

finally:
    print("Resource Closed")

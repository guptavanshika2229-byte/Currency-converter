a=int(input("enter a number = "))
def fib(a):
    if a==1:
        return 1
    elif a==2:
        return 2
    else:
        return fib(a-1)+fib(a-2)
print(fib(a))
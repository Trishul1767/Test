#n=list(map(int,input("enter the numbers").split()))
#fibonacci series
n=int(input())
a=0
b=1
for i in range(n):
    print(a)   
    a,b=b,a+b
#fibonacci series using recursion
def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_series=fibonacci(n-1)
        fib_series.append(fib_series[-1]+fib_series[-2])
        return fib_series
n=int(input())
print(fibonacci(n))

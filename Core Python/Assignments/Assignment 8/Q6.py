# Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms
def fibonacci(num):
    a=-1
    b=1
    sum=0
    for i in range(1,num+1):
        c=a+b
        a=b
        b=c
        sum+=c
    print(sum)
fibonacci(5)
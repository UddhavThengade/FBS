# WAP to print Fibonacci series upto n.
a=-1
b=1
num = int(input('Enter The Number : '))
for i in  range(num+1):
    c=a+b
    print(c)
    a=b
    b=c
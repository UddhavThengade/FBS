# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
def sum_of_range(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    print(f'Sum of Range is : {sum}')
sum_of_range(5)


# b. 1!+ 2! + 3! + 4!+..... + n!
def fac(num):
    fac=1
    for i in range(1,num+1):
        fac*=i
    print(f'Factorial of {fac}')
fac(5)


# c. 1^1 + 2^2 + 3^3+ ...... n^n
def exp(num):
    exp=1
    for i in range(1,num+1):
        exp+=(num**i)
    print('output',exp)
exp(3)
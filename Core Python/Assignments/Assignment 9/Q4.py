# WAP to find sum of n number using recursion 
def sum_n(n):
    if n==0:
        return 0 
    return n+sum_n(n-1)
n=int(input('enter number : '))
print('sum =',sum_n(n))
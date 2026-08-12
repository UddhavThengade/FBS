# Write a program to find sum of digits of a number.
def sum_digit(num):
    sum=0
    while(num>0):
        d=num%10
        sum=sum+d
        num//=10
    print(sum)
sum_digit(8)

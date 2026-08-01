# Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!


num=int(input('Enter The Number : '))
mul=1
sum=0
for i in range (1,num+1):
    mul=mul*i
    sum=mul+sum
print(sum)


#**************B**************

# N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

num = int(input('Enter The Number : '))
pw=0
for i in range(1,num+1):
    pw=pw+(num**i)
print(pw)



#*************C*****************


# Find the sum of a geometric series from 1 to n where the common ratio is 2.

s=0
num=int(input('Enter The Number : '))
for i in range(num):
    s=s+(2**i)
print(s)



#**************D****************

# S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a=int(input('Enter Number : '))
s=0
for i in range(1,11):
    s=s+(a**i)/i
print(s)



#----------------E---------------
# x - x2/3 + x3/5 - x4/7 + .... to n terms

k=1
sum=0
x=int(input('Enter X value : '))
n=int(input('Enter Range '))
for i in range(1,n+1):
    if(i%2!=0):
        sum=sum-(x**i)/k
        k+=2
    else:
        sum=sum+(x**i)/k
        k+=2
print(sum)


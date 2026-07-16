# Write a program to check if given 3 digit number is a palindrome or not.
num = int(input('Enter The 3 Digit Number : '))
digit=num
d1=num%10
num=num//10
r1 =d1*100

d2=num%10
num=num//10
r2 = d2*10

d3 = num
r3 = d3*1
sum=r1+r2+r3
print(r1,r2,r3,sum)
if(sum==digit):
    print('palindrone')
else:
    print('Not Palindrone')


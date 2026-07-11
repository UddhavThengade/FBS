#Find the sum of three-digit number.
num = int(input('Enter The 3 Digit NO. : '))
numm =num
a=num%10
num=num//10
b = num%10
num = num//10
print(f'you are enter this 3 digit number-{numm} and this number sum is : {a+b+num}')
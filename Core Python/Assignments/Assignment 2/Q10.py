#Write a program to reverse three-digit number.
num = int(input('Enter three Digit Number : '))
numm=num
a=num%10
R_a = a*100
num=num//10
b = num%10
R_b = b*10
num=num//10
R_c = num*1
print(f'The {numm} is the reverce value is : {R_a+R_b+R_c}')

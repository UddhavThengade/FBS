#Write a program to swap two numbers using third variable.
a = int(input('Enter the 1 number A = : '))
b = int(input('Enter the 2 number B = : '))
print(f'Number Before Using Swapping A= {a}, B= {b}')
c=a
a=b
b=c
print(f'number After Using Swapping A ={a},B={b}')

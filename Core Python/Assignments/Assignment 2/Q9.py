#Write a program to swap two numbers without using third variable.
a = int(input('Enter The Num A = : '))
b = int(input('Enter The Num B = : '))
print(f'the number before swapping A={a},B={b}')
a=a+b
b=a-b
a=a-b
print(f'the number after swapping A={a},B={b}')
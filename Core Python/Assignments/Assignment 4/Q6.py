# WAP to check if a given number is prime number or not.

num=int(input('Enter The Number : '))
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        print('Not Prime')
    else:
        print('Prime')
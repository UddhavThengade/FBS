# WAP to print all numbers in a range divisible by a given number.
num1=int(input('Enter The start of Number : '))
num2=int(input('Enter the End of Number'))
num3=int(input('enter The divisible of the no.:'))
for i in range(num1-1,num2+1):
    if(i%num3==0):
        print(i)
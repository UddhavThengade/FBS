# Write a program to check if given number is Armstrong number or not.
num = int(input('Enter the Number : '))
numm=num
total=0
length=len(str(num))
while(num>0):
    d=num%10
    num=num//10
    pow=d**length
    total=total+pow
if(total==numm):
    print('Amrstrong no.')
else:
    print('Not Amrstrong No.')
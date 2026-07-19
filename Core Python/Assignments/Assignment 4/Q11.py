# WAP to check if given number Strong Number.
num = int(input('Enter The Number : '))
total=0
numm=num
while(num>0):
    d=num%10
    num=num//10
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    total=total+fact
if(total==numm):
    print('strong no')
else:
    print('Not Strong No.')


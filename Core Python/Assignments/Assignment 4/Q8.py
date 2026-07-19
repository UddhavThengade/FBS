# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

num = int(input('Enter The Number : '))
for i in range (num+1):
    if(i%7==0 or i%5==0):
        print(i)
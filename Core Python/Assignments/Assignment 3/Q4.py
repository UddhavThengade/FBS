#WAP to input the all sides of a triangle and cheak whether triangle is valid or not 
a = int(input('Enter The Angle 1 : '))
b= int(input('Enter The Angle 2 : '))
c = int(input('Enter The Angle 3 : '))
if(a+b>c and a+c>b and c+b>a and a>0 and b>0 and c>0 and a+b+c==180):
    print('Triangle is Valid.')
else:
    print('Triangle is Invalid') 
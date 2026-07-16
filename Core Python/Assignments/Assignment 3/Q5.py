#WAP to cheak whether the triangle is equilateral,isosceles,scalene ?
a = int(input('Enter The Angle 1 : '))
b = int(input('Enter The Angle 2 : '))
c = int(input('Enter The Angle 3 : '))
if(a==b and b==c and a==c and a+b+c==180):
    print('equilateral')
elif(a==b or b==c or a==c) and a+b+c==180:
    print('Isosceles')
elif(a!=b and b!=c and a!=c and a+b+c==180):
    print("scalene")
else:
    print('Not Valid Tringle')

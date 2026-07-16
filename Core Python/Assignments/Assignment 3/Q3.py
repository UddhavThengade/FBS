#WAP to in put angles of tringle and cheak whether tringle is valid or not

angle_1 = int(input('Enter the angle 1 : '))
angle_2 = int(input('Enter the angle 2 : '))
angle_3 = int(input('Enter The angle 3 : '))
if(angle_1>0 and angle_2>0 and angle_3>0 and (angle_1+angle_2+angle_3==180)):
    print('Triangle is valid')
else:
    print('Triangle is Invalid')
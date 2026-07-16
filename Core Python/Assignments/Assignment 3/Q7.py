#WAP to cheak if user has entered currect userid and password?
userid = 'uddhav@123'
password = '12345'

a = input('Enter The Userid : ')
b = input('Enter the Password : ')
if(a==userid and b==password):
    print('Currect Userid And Password.')
else:
    print('Incurrect Information')
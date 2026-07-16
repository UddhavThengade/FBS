# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random
userid = 'uddhav@123'
password = '12345'
id = input('Enter The Userid : ')
pas = input('Enter The Password : ')
if(userid==id and password==pas):
    captcha = random.randint(1000,9999)
    print('Your Captcha is',captcha)
    a=int(input('Enter The Captcha'))
    if(captcha==a):
        print('Successfully Login')
    else:
        print('Invalid captcha')
else:
    print('Invalid Information')
    
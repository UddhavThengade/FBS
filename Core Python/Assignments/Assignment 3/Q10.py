# Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

age = int(input('Enter Your Age : '))
gender = input('Enter The Gender(Male/Female) : ')
if(gender=='Male'):
    if(age>=21):
        print('You Eligible For Marry.')
    else:
        print('You are Not Eligible For Marry. ')
elif(gender=='Female'):
    if(age>=18):
        print('You Are Eligible For Marry.')
    else:
        print('You Are Not Eligible For Marry.')
else:
    print('Invalid Input.')

# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

a = int(input('Enter The Mark Of Frist Subject :'))
b = int(input('Enter The Mark Of secound Subject :'))
c = int(input('Enter The Mark Of thired Subject :'))
d = int(input('Enter The Mark Of fourth Subject :'))
e = int(input('Enter The Mark Of Fipth Subject :'))
per = ((a+b+c+d+e)/500)*100
if (per>=90):
    print('Frist Class',per)
elif(per>=80):
    print('Secound Class',per)
elif(per>=70):
    print('Thired class',per)
elif(per>=60):
    print('Fourth Class',per)
else:
    print('FAIL')
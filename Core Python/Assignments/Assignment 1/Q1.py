# WAP to calculate the Percantage of student based on mark of any 5 subject.

print('Enter the Five Sub marks')
sub1 = int(input('Marathi : '))
sub2 = int(input('English : '))
sub3 = int(input('Math : '))
sub4 = int(input('Biology : '))
sub5 = int(input('Physics : '))

sum = sub1+sub2+sub3+sub4+sub5
per = (sum/500)*100
print('Your Percantage is :',per)

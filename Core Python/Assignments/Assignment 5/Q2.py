# Q2.Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.


stu = int(input('enter the student no: '))
for i in range(1,stu+1):
    sub1=int(input('Enter The Marathi Sub Mark : '))
    sub2 = int(input('Enter The English Sub mark : '))
    sub3 = int(input('Enter The Biology Sub Mark : '))
    sub4 = int(input('Enter The Math Sub Mark : '))
    sub5 = int(input('Enter The Physics Sub Mark : '))
    sum=(sub1+sub2+sub3+sub4+sub5/500)*100
    print('The Student Percentage Is ',sum)
i+=1
# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


age1 = int(input('Enter The Frist Person Age : '))
amt1 = float(input('Enter The Tiket Price Of Person 1 :'))
if(age1<=12):
    dis1=amt1*0.3
    t1=amt1-dis1
elif(age1>=59):
    dis1=amt1*0.5
    t1=amt1-dis1
else:
    t1=amt1
#first person End
age2 = int(input('Enter The Seound Person Age : '))
amt2 = float(input('Enter The  Tiket Amount Of person 2 : '))
if(age2<=12):
    dis2=amt2*0.3
    t2=amt2-dis2
elif(age2>=59):
    dis2=amt2*0.5
    t2=amt2-dis2
else:
    t2=amt2
age3 = int(input('Enter The Thired Person Age : '))
amt3 = float(input('Enter The Tiket Amount Of Person 3 : '))
if(age3<=12):
    dis3=amt3*0.3
    t3=amt3-dis3
elif(age3>=59):
    dis3=amt3*0.5
    t3=amt3-dis3
else:
    t3=amt3
age4 = int(input('Enter The Fourth Person Age : '))
amt4 = float(input('Enter The Tiket Amount Of Person 4 : '))
if(age4<=12):
    dis4=amt4*0.3
    t4=amt4-dis4
elif(age4>=59):
    dis4=amt4*0.5
    t4=amt4-dis4
else:
    ts4=amt4
age5 = int(input('Enter The Fifth Person Age : '))
amt5 = float(input('Enter the Tiket Amount of person 5 : '))
if(age5<=12):
    dis5=amt5*0.3
    t5=amt5-dis5
elif(age5>=59):
    dis5=amt5*0.5
    t5=amt5-dis5
else:
    t5=amt5

sum = t1+t2+t3+t4+t5
print('Your Total Amount Is The ',sum)
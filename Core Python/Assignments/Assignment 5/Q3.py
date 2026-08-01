# Q3.Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

p1=int(input('Enter no of passenger : '))
cost=int(input('Enter The cost of Tiket : '))
sum=0
for i in range(1,p1+1):
    age=int(input('Enter the Age : '))
    i+=1
    if(age<=12):
        sum=cost*0.3
        print(sum)
    elif(age>59):
        sum=cost*0.5
        print(sum)
    else:
        sum=cost
        print(cost)
print('Your Total bill Is ',sum)
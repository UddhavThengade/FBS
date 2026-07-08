# WAP to calculate Area of ractangle

# length = int(input('enter the length :'))
# wigth = int(input('enter the wigth :'))

# area = length*wigth
# print(f'area of the ractangle is :,{area}')


#****************#


#WAP to enter P,T,R  and calculate the simple intrest

# p = int(input('enter the principal of amount :'))
# r = int(input('enter the rate of intrest : '))
# t = int(input('enter the time of intrest : '))
# sum =(p*r*t/100)
# print(f"simple intrest is :,{sum}")

#***************#



#Quotient and reminder

# divident = int(input('enter the devident :'))
# divisor = int(input('enter the divisor :'))

# q = divident//divisor
# r = divident % divisor
# print('Quotient',q)
# print('Reminder',r)


#*****************#


# days = int(input('enter the days :'))
# years = days // 365
# days = days % 365
# weeks = days // 7
# days = days % 7
# print(f'years,{years} weeks,{weeks} days,{days}')


num = int(input('enter the three digit no : '))
d1 = num %10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num //10
sum = d1+d2+d3
print(sum)
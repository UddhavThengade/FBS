# WAP to cheak if entered year is leap year or not 
def leap_year(num):
    if(num%400==0) or (num%4==0 and num%100!=0):
        print('Leap year')
    else:
        print('NOt Leap Year')
leap_year(2024)
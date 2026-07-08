#WAP to enter P,T,R and calculate compound Interest.

p = float(input('Enter the principal : '))
r = float(input('Enter the rate of principal : '))
t = float(input('Enter the time of years : '))
total=p*(((1+r/100))**t)-p
print('your compound Interest is : ',total)
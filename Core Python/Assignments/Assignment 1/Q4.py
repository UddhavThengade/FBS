#WAP to enter the P,T,R and calculate simple Interest

p = int(input('Enter the principal of amount : '))
r = int(input('Enter the Rate of Intrest : '))
t = int(input('Enter the time of years : '))

total = (p*r*t)/100
print('your simple Interest is : ',total)
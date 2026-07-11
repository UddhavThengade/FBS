#WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.'''
sallary = float(input('Enter The Your Based Sallary : '))
da = (sallary*10)/100
ta = (sallary*12)/100
hra = (sallary*15)/100
total_sallary = sallary+da+ta+hra
print(f'employed Base Sallary is : {sallary} \n After 10% da {da} \n ta 12% {ta} \n hra 15% {hra} \n total sallary is {total_sallary}')


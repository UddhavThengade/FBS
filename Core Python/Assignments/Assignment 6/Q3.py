from math import factorial
for i in range(4):
     for space in range (1,4-i):
        print(' ',end=' ')
     for j in range(i+1):
          ncr=factorial(i)//(factorial(j)* factorial(i-j))
          print(ncr,end='  ')
     print()

    
    
#WAP to cheak if entered number is palindrome or not.
def pal_num(num):
    rev=0
    numm=num
    while(num>0):
        d=num%10
        rev=rev*10+d
        num//=10
    if(numm==rev):
        print('Number is palindrome')
    else:
        print('Number is Not palindrome')
pal_num(211)
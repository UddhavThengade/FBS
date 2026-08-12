#WAP find reverse of a number
def num_rev(num):
    rev=0
    while(num>0):
        d=num%10
        rev=rev*10+d
        num//=10
    print(rev) 
num_rev(123)
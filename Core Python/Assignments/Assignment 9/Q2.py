# WAp to cheak if given number is Armstrong or not armstrong using recursive function
def ams(n,pw):
    if(n==0):
        return 0
    d=n%10
    return d** pw + ams(n // 10 , pw)
num=int(input('Enter The Number : '))
d=len(str(num))
res=ams(num,d)
if(res==num):
    print('Armstrong Number ')
else:
    print('NOT Armstrong Number ')

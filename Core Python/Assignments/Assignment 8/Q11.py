# WAP to cheak number is amstrong or not 
def chek_ams(num):
    n=num
    length=len(str(n))
    total=0
    while(num>0):
        d=num%10
        pow=d**length
        num//=10
    if(total==n):
        print('Number is Amstrong')
    else:
        print('Number Is Not Amstrong')
chek_ams(154)
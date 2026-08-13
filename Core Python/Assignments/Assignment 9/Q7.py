# WAP to find sum of digit using recurive
def sum(num):
    if(num==0):
        return 0
    else:
        d=num%10
        return d+sum(num//10)
print(sum(133))
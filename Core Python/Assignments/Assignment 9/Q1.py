# Wap to find sum of following serires using recursive function 
# i 1! + 2! + 3! + 4! +.....+n!
# Note for fact and sum two recursive function 
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1) 

def sum(n):
    if n==1:
        return 1
    return fact(n)+sum(n-1)

result=sum(10)
print('sum : ', result )
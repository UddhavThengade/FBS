# WAP to cheak whether a number is prime or not using recursive
def prime(num,i=2):
    if(num<2):
        return False
    if (i*i>2):
        return True
    if(num%i==0):
        return False
    return prime(num,i+1)
print(prime(1))
    
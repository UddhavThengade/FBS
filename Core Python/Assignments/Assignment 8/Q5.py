# Sum of all prime numbers between 1 to n

def prime(num):
    sum_prime=0
    for i in range(2,num+1):
        prime=True
        for j in range(2,i):
            if i % j == 0:
                prime= False
                break
            if prime:
                sum_prime+=i
    print(sum)
prime(6)
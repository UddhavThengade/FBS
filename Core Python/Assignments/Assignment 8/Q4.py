# Sum of all odd numbers between 1 to n
def odd_num(num):
    sum=0
    for i in range(1,num+1):
        if(i%2!=0):
            sum+=i
    print(f'sum of odd number is : {sum}')
odd_num(8)
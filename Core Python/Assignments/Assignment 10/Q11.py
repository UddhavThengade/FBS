# Write a program to print all numbers which are divisible by m and n in the
# list.
def number(li):
    m=int(input('Enter The Number : '))
    aa=[]
    n=int(input('Enter The Number : '))
    bb=[]
    for i in range(len(li)):
        if(i % m ==0):
            aa.append(li[i])
        if(i % n ==0):
            bb.append(li[i])
    print(aa,bb)
li=[1,2,3,4,5,6]
print(li)
number(li)

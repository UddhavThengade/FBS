# Write a program to find sum of all elements of list
def sum(li):
    sum=0
    for i in range(0,len(li)):
        sum+=li[i]
    print('Total Sum Is ',sum)
li=[1,2,4,3,5,6,9]
sum(li)
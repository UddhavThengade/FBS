# Write a program to remove all occurrences of a given element in the list.
li=[1,2,3,4,5,6,4,1]
n=int(input('Enter The Number : '))
for i in range(len(li)-1,-1,-1):
    if(li[i]==n):
        li.remove(li[i])
print(li)
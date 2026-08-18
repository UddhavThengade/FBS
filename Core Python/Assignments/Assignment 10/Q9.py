# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.
li=[]
even=[]
odd=[]
n=int(input('Enter The no of range : '))
for i in range(0,n):
    e1=int(input('Enter Element : '))
    li.append(e1)
print(li)
for i in range(0,len(li)):
    if(li[i]%2==0):
        even.append(li[i])
    else:
        odd.append(li[i])
print('Odd',odd)
print('even',even)
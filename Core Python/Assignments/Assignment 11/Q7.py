# python program to find the intersection of two lists
li1=[1,2,3,4,5]
li2=[3,4,5,6]
for i in range(len(li1)-1,-1,-1):
    if(li1[i] not in li2):
        li1.pop(i)
print(li1)
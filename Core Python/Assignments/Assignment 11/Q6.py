# python program to find union of two lists
li1=[2,3,4,5,6]
li2=[1,2,3,8]
li1.extend(li2)
for i in range(len(li1)-1,-1,-1):
    for j in range(i+1):
        if(i!=j and li1[i] == li1[j]):
            li1.pop(i)
print(li1)
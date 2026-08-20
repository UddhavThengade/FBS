# python program to sort a list acording to the length of the element within the list

li=['apple','banana','tree','telephone']
for i in range(len(li)-1):
    for j in range(0,len(li)-1):
        if(len(li[j]) > len(li[j+1])):
            temp=li[j]
            li[j] = li[j+1]
            li[j+1] = temp
print(li)
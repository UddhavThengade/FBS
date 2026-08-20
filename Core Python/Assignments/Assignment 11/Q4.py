# phyton program to find secound largest number in a list using bubble sort
li=[1,2,7,85,4,3,533,89,65]
for i in range(0,len(li)-1):
    for j in range(0,len(li)-i-1):
        if(li[j] > li[j+1]):
            temp=li[j]
            li[j] = li[j+1]
            li[j+1] = temp
    print(li)
print(li[len(li)-2])
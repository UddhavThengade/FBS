# Write a program to remove duplicates from the list.
def remove(li):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if(li[i]==li[j]):
                li.pop(j)
                break
    print(li)
li=[12,2,12,3,2,1,33,42,122,2]
remove(li)

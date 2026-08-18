# Write a program to create a new list from existing list which contains cube of
# each number of list.
def new_list(li):
    cube=0
    l2=[]
    for i in range(0,len(li)):
        cube=li[i]**3
        l2.append(cube)
    print(l2)
    # print(res)
li=[1,2,3,4,5]
new_list(li)
# Write a program to create three lists of number their sqares and cubes
l1=[1,2,3,4,5,6,7,8]
print('original List : ',l1)
l2=[]
l3=[]
sq=0
cube=0
for i in range(len(l1)):
    sq=l1[i]**2
    l2.append(sq)
    cube=l1[i]**3
    l3.append(cube)
print('Square',l2)
print('Cube',l3)
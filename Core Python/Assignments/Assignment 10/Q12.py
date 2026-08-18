# Write A Program to create three lists of numbers Their squres
# and cube
li=[1,2,3,4,5,6,7,8,9]
sq=0
cu=0
square=[]
cube=[]
for i in range(len(li)):
    sq=li[i]**2
    square.append(sq)
    cu=li[i]**3
    cube.append(cu)
print(f'Square OF List : {square}')
print(f'cube Of List : {cube}')

# Python Program to put even and odd element of list into two diffrent lists

li=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in range(0,len(li)):
    if(li[i]%2 == 0):
        even.append(li[i])
    if(li[i]%2 != 0):
        odd.append(li[i])
print('even list ',even)
print('Odd List ',odd)
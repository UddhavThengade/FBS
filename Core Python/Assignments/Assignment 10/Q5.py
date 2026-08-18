# Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.
def present(li):
    n=int(input('Enter The Number : '))
    count=0
    for i in range(0,len(li)):
        if(li[i]==n):
            count+=1
            
    if(count >0):
        print(f'Number Is Found & This Number Is {count} times')

    else:
        print('Number Not found')
li=[1,2,3,4,5,6,6,7,1,2,0,7,8,9,0]
present(li)
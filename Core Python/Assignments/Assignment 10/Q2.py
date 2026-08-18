# Write a program to find maximum and minimum element in a list.
def max(li):
    max=li[0]
    min = li[0]
    for i in range(1,len(li)):
        if(li[i] > max):
            max=li[i]
        if(li[i] < min):
            min=li[i]
    print('This Is Max number : ',max)
    print('This Is Min Number : ',min)
li=[2,12,34,566,2234,13]
max(li)
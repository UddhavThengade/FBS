# Write a program to find the second largest element in the list.
def sec_large(li):
    li.sort()
    print(li)
    print(li[len(li)-2])
li=[10,4,9,2,8]
sec_large(li)
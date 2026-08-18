# Write a program to create a duplicate of an existing list. It should not point to
# same list.
li1=[1,2,3,4,5]
li2=li1.copy()
li2.append(6)
print('This Is Orignal List ',li1)
print('this is Duplicate List',li2)

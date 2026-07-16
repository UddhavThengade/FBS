#WAP to profit and loss?
cost_p = int(input('Enter The Cost Price : '))
sel_p = int(input("Enter The Selling Price : "))
if(cost_p<sel_p):
    print('Profit')
elif(cost_p==sel_p):
    print('No Prfit No Loss')
else:
    print('Loss')
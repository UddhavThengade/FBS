#WAP to calculate selling price of book based on cost price and discount.
cost = float(input('Enter The Cost Price of Book : '))
dis = float(input('Enter The Discount percentage of book : '))
dis_val = (cost*dis)/100
sell_pri = cost-dis_val
print(f'the book cost Price is : {sell_pri}')
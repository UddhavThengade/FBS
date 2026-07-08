#program to find the Roots of Quadratic Equation.
a = int(input('Enter the Coefficient of x2 : '))
b = int(input('Enter the Coefficient of x : '))
c = int(input('Enter the Constant term : '))

root = (-b+(b**2-4*a*c)**0.5)/(2*a)
root1 =(-b-(b**2-4*a*c)**0.5)/(2*a)

print('Roots of Quadratic equation is :',root,root1)

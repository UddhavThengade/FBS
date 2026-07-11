#Convert distant given in feet and inches into meter and centimeter.
feet = float(input('Enter the Feet : '))
inches = float(input('Enter The Inches : '))
total_inches = (feet*12)+inches
meter = total_inches*0.0254
cent = total_inches*2.54
print(f'{feet} and {inches} is {meter:.2f} meter and {cent:.2f} centimeter')
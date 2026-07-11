#Convert the time entered in hh,min and sec into seconds.
hours = int(input('Enter The Hours : '))
min = int(input('Enter The Min : '))
sec = int(input('Enter The Sec : '))
secound = (hours*3600)+(min*60)+sec
print(f'Total Secound in the gievn time {hours}:{min}:{sec} is :',secound)

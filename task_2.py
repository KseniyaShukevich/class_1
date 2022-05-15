seconds = int(input('Enter number of seconds: '))

hours = seconds // 60 // 60
minutes = seconds // 60 % 60
seconds = seconds % 60

print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

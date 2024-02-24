try:
    x = int(input('x: '))
    y = 1/x
    
except ZeroDivisionError:
    print('cannot divided by zero')
else:
    print('y = ', y)
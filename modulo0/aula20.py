def eq():
    a1 = input('digite o valor de a: ')
    if a1.isnumeric:
        a = float(a1)
    else:
        print('digite apenas números.')

    b1 = input('digite o valor de b: ')
    if b1.isnumeric:
        b = float(b1)
    else:
        print('digite apenas números.')

    c1 = input('digite o valor de c: ')
    if c1.isnumeric:
        c = float(a)
    else:
        print('digite apenas números.')
    return b**2 - 4*a*c

q = eq()
print(q)
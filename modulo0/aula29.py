n = int(input('digite um número: '))
if (n >= 0):
    if (n % 2) == 0:
        print(n, 'é par positivo')
    else:
        print(n, 'é ímpar positivo')
else:
    if (abs(n) % 2) == 0: 
        print(n, 'é par negativo')
    else:
        print(n, 'é ímpar negativo')

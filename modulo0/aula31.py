numero = int(input('Digite um número: '))
if numero > 0:
    if (numero % 2) == 0:
        print(f'{numero} é par...')
    else:
        print(f'{numero} é ímpar...')
else:
    print(f'{numero} é igual ou menor que zero.')

numero = int(input('Digite um números: '))
fatorial = 1
if numero < 0:
    print(f'O fatorial de {numero} não existe.')
elif numero == 0:
    print(f'O fatorial de {numero} é igual a 1')
else:
    for i in range(1, numero + 1):
        fatorial *= i
    print(f'O fatorial de {numero} é igual a {fatorial}')
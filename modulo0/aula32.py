altura = float(input('digite sua altura: '))
genero = input('Qual é o seu género? <F ou M: ')
if (genero == 'F'):
    peso = (62.1 * altura) - 44.7
else:
    peso = (72.7 * altura) - 58
print(f'O seu peso é {peso} kg')
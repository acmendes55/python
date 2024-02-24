idade = 0
soma = 0
quantidade = 0

while idade != -1:
    idade = int(input(f'digite a idade {quantidade +1}: '))
    if idade != -1:
        soma += idade
        quantidade += 1
if quantidade == 0:
    print('Não foi digitada idade alguma.')
else:
    media = soma/5
    print(f'A média das {quantidade} é: {media}')
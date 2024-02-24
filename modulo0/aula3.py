idade = int(input('Digite a sua idade: '))

preco = 10

if (idade <12 or idade >=65):
    print('Entrada a 0 euros.')

elif (idade >= 12 and idade <18):
    print('entrada a' + str(preco / 2) + ' euros')
else:
    print('entrada a ' + str(preco) + ' euros')
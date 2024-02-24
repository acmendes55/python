lista = []
idade = -1
while (idade != 0):
    idade = int(input('Digite a tua idade: '))
    if (idade != 0):
        lista.append(idade)

print('soma das idades: ', sum(lista))
print('O mais novo: ', min(lista))
print('O mais velho: ', max(lista))
print(lista)
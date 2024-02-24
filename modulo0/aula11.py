cidades = input('introduza as cidades: ')

lista_cidades = cidades.split(',')
lista_cidades.sort()

for c in lista_cidades:
    print(c)


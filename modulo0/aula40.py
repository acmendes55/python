lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(type(lista_de_numeros))
#print(dir(lista_de_numeros))

lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8]
# concatenação +
lista3 = lista1 + lista2
print(lista3)

# Repetição *
lista4 = lista3*4
print(lista4)

print(5 in lista4)

frase = 'um texto qualquer'
lista_caracteres = list(frase)
print(lista_caracteres)
print(lista1[::-1])
print(len(lista1))
print(sum(lista1))
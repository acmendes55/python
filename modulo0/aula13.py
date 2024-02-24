def pow(lista, a):
    for i in range(len(lista)):
        lista[i] = lista[i] ** a
    return lista
lst = [1, 3, 5, 7, 9]

print(lst)
#print(pow(lst, 2))
pow(lst, 2)
print(lst)
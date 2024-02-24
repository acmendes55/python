text = 'O meu carro é uma discoteca'

"""
print(len(text))

i = 0

while (i < len(text)):
    print(text[i])
    i += 1
    
"""

"""
indice = 0

while (indice < len(text)):
    if (text[indice] == 'a'):
        print('indice:', indice, 'caracter:', text[indice])
        break
    indice += 1
"""
indice = 0

while (indice < len(text)):
    if (text[indice] != 'a'):
        print(text[indice])
    indice += 1

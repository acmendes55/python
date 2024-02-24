"""
Fazer um programa que:
    - faça um programa que receba uma quantidade variável de strings (termine a digitação com string vazia = '');
    - guarde essas informações em uma lista;
    - crie uma outra lista onde cada elemento ( palavra) se transformará numa lista de caracteres únicos, 
    - em seguida, mostre a lista modificada.
"""
palavras = list()
lista = list()

while True:
    palavra = input('Digite uma palavra: ')
    if palavra == '':
        break
    else:
        palavras.append(palavra)
for palavra in palavras:
    lista.append(list(set(palavra)))

for item in lista:
    print(item)
"""
Fazer um programa que:
    - recebe a quantidade ilimitada de idades de pessoas;
    - guarde essas idades numa lista;
    - para encerrar a digitação das idades deve digitar-se -1;
    - em seguida, deve gerar-se uma tupla de idades, a partir da lista;
    - deve mostrar-se as seguintes informações :
        - quantidade de idades digitadas;
        - média das idades.
"""
lista_idades = list()
while True:
    idade = int(input('Digite a tua idade: '))
    if idade != -1:
        lista_idades.append(idade)
    else:
        break
tupla_idades = tuple(lista_idades)
qtd = len(tupla_idades)
total = sum(tupla_idades)
media = total/qtd
print(f'O total de idades digitadas é {qtd}')
print(f'A média das idades é {media}')
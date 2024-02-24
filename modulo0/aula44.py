"""
Fazer um programa que:
    - receber o cadastro de uma quantidade ilimitada de proprietários e seus respectivos apartamentos (número de apartamento e nome dos propritário);
    - guardar essas informacções em dicionário em que a chave de busca é o números do apartamento;
    para encerrar a digitação o número do apartamento será -1;
    - em seguida, deve mostrar-se uma listagem em ordem crecente de apartamento: apartamento - nome do proprietário;
    - no final, apresente a quantidade total de apartamentos listados.
"""

proprietarios = dict()
while True:
    apartamento = int(input('Digite o apartamento: '))
    if apartamento != -1:
        proprietario = input('Proprietários: ')
        proprietarios.update({apartamento : proprietario})
    else:
        break

edificio = dict(sorted(proprietarios.items()))

for chave, valor in edificio.items():
    print(f'{chave} - {valor}')

print(f'Total de apartamentos: {len(edificio)}')
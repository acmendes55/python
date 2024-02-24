"""
Fazer um programa que:
    - receba as informações (nome, idade, e numero de calçado) de 5 pessoas distintas;
    - depois de receber estas informações, mostre a relação completa das pessoas e as suas informações, em ordem alfabética de nome;
    - Ao final do relatório, voce deve calcular e mostrar as seguntes informações:
        - a média da idade das pessoas;
        o número médio do calçado das pessoas pesquisadas.
"""
pessoas = list()
for i in range(1, 6):
    print(f'Pessoa {i}: ')
    nome = input('Digite o nome: ')
    idade = int(input('Quantos anos tem: '))
    calcado = int(input('Quanto calça: '))
    print('-----------------------------------------------')
    pessoa = [nome, idade, calcado]
    pessoas.append(pessoa)
nova_lista = sorted(pessoas)
total_idades = 0
total_calcados = 0
print('Relação das pessoas e suas informações...')
for i in range(0, 5):
    total_idades += nova_lista[i][1]
    total_calcados += nova_lista[i][2]
    print(f'{nova_lista[i][0]} - {nova_lista[i][1]} - {nova_lista[i][2]}')
print('-----------------------------------------------')
print(f'Média das idades: {total_idades/5}')
print(f'Número médio dos calçados: {int(total_calcados/5)}')

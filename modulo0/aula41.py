"""
Fazer um programa que:
    - receba a quantidade ilimitada de nomes de cidades e guarde esses nomes em uma lista;
    - para encerrar a digitação das cidades deve digitar-se : sair;
    - em seguida, deve ordenar-se essa lista de cidades em ordem crescente;
    - mostrar a relação nominal das cidades ordenadas 1 por linha.
"""
cidades = list()
while True:
    cidade = input('Digita o nome de uma Cidade: ')
    if cidade == 'sair':
        break
    else:
        cidades.append(cidade)
if len(cidades) > 0:
    cidades.sort()
    for cidade in cidades:
        print(cidade)
else:
    print('A lista de cidades está vazia')
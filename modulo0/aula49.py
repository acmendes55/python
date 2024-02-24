def potencia(base, expoente = 1):
    '''Função que calcula a potência de um número'''
    resultado = pow(base, expoente)
    return resultado
n = float(input('Digite a base: '))
e = int(input('Digite o expoente: '))
print(f'{potencia(n, e)}')
print(f'{potencia(n)}')
print('------------------------------')


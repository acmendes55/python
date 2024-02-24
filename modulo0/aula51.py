"""
Faça uma função em python que retorne o valor lógico True se o número inteiro passado por parâmetro for primo e falso caso contrário.
"""
def primo(numero):
    '''Função lógica que retorna true se o valor for primo'''
    eprimo = False
    resto_zero = 0

    for i in range(1, numero):
        if (numero % i) == 0:
            resto_zero +=1
    
    if resto_zero ==1:
        eprimo = True
    return eprimo
n = int(input('Digite um valor: '))
if primo(n):
    print(f'o número {n} é primo.')
else:
    print(f'o número {n} não é primo.')

def soma(*args):
    total = 0
    for i in args:
        total += i
    return total

print(soma(1,2,3,4,5,6,7,8,9,10))

print('------------------------')

def soma(*args):
    total = sum(args)
    return total

print(soma(1,2,3,4,5,6,7,8,9,10))

print('------------------------')

def comida_favorita(**kwargs):
    for chave in kwargs:
        print(f'{chave} gosta de {kwargs[chave]}')

comida_favorita(Madalena = 'Bacalhau', MArcelo = 'Risoto', Adriana = 'Camarão')

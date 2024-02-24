def peso():
    gen = input('Digite um Género: ')
    altura = float(input('Quanto mede: '))
    h = (72.7*altura) - 58
    m = (62.1*altura) - 44.7
    if (gen == 'H'):
        return h
    else:
        return m
p = peso()
print(f'O seu peso é {p} kg')
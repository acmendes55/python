def mont():
    c = float(input('Capital: '))
    r = float(input('Taxa: '))
    t = float(input('Tempo: '))
    m = c*(1 + r/100)**t - c
    return m
m1 = mont()
print(m1)
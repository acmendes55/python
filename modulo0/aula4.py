def funcao_area(comprimento, largura):
    area = comprimento * largura
    return area

def funcao_perimetro(comprimento, largura):
    perimetro = 2 * (comprimento + largura)
    return perimetro

c = int(input('Comprimento: '))
l = int(input('Largura: '))

area = funcao_area(c, l)
perim = funcao_perimetro(c, l)

print(f'A área da figura é: {area}')

print(f'o seu perímetro é: {perim}')

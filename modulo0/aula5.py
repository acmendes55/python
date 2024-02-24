def funct_area(comp, larg):
    area = comp * larg
    return area

c = int(input('Comprimento: '))
l = int(input('Largura: '))

a = funct_area(c, l)
print(a)
def area_cilindro(raio, altura):
    def area_circulo(raio):
        PI = 3.141592
        area = PI * pow(raio, 2)
        return area
    area = area_circulo(raio)*altura
    return area

r = float(input('Digite o valor do raio: '))
h = float(input('Digite o valor da altura: '))
a = area_cilindro(r, h)
print(f'O valor da área do cilindro de raio {r} e altura {h} é igual a {a}')
print('---------------------------')

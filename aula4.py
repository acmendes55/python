def valor_futuro_simples():
    capital = float(input('valor total a investir: '))
    tempo = float(input('tempo do investimento em anos: '))
    taxa = float(input('taxa proposta pelo banco: '))
    juro = (1 + tempo*(taxa/100))*capital
    return juro
v1 = valor_futuro_simples()
print(f' o juro a ser pago na maturidade do investimento é {v1}')


def valor_futuro_composto():
    capital = float(input('valor total a investir: '))
    tempo = float(input('tempo do investimento em anos: '))
    taxa = float(input('taxa proposta pelo banco: '))
    juro = ((1 + (taxa/100*tempo))**tempo) *capital
    return juro
v2 = valor_futuro_composto()
print(f' o juro a ser pago na maturidade do investimento é {v2}')
txt_in = 'Huambo;Luanda;Cabinda;Aveiro;Lisboa'

cidades = txt_in.split(';')

#cidades.sort()# ordena por ordem alfabética(altera a lista original)
#cidades.sort(key = len, reverse = True)# ordena por ordem alfabética(altera a lista original)
cidades.sort(key = len, reverse = True)# ordena por ordem alfabética(altera a lista original)
#x = sorted(cidades) # cria uma nova lista ordenada (mantém a original)

for c in cidades:
    print(c)

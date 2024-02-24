text = 'O meu carro é uma discoteca'

count = 0
for i in range(len(text)):
    if text[i] == 'a':
        count += 1
        continue
    print(i, text[i])
print('O texto tem ' + str(count) + 'letras a')
soma = 0
i = 1
while i <= 5:
    idade = int(input(f'Digite a idade {i}: '))
    soma += idade
    i += 1
media = soma/5
print(f'A média das idades é {media} anos de idade.')

#soma += idade --> soma = soma + idade
# i += 1 --> i = i + 1
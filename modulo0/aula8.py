idade = -1

while (idade < 0 or idade > 150):
    idade = int(input('Digite a sua idade: '))
    if (idade <0 or idade >150):
        print('idade inválida. Digite novamente [0-150]!')
if (idade<10):
    print('Você é criança...')
idade = int(input('Digite a sua idade: '))

if (idade < 12):
    print('você é uma criança.')
else:
    if (idade >= 12 and idade < 18):
        print('você é um(a) adolescente.')
    else:
        if (idade >= 18 and idade <65):
            print('você é um adulto.')
        else:
            print('você é um senior.')
        
nome = input('Olá? Qual é o teu nome: ')
idade = int(input('Quantos anos tens: '))
altura = int(input('Quanto mede: '))
peso = int(input('Quantos pesa: '))
sapato = int(input('Quanto calça: '))
imc = peso / altura **2
print(f'O meu nome é {nome}, tenho {idade} anos de idade, meço {altura} metros de altura, peso {peso} kg, calço tamanho {sapato} e o meu imc é {imc}!')
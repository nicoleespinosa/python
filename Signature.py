# Nicole Espinosa, RM:96201

nome = input('Olá! Insira seu nome completo, por favor: ')
assin = input('A sua assinatura é BASIC, SILVER, GOLD ou PLATINUM? ')
faturamento_anual = float(input('Qual foi o faturamento do seu canal seu ano? '))

desconto = 0
if assin.upper() == 'BASIC':
    desconto = faturamento_anual * 0.3

elif assin.upper() == 'SILVER':
    desconto = faturamento_anual * 0.2

elif assin.upper() == 'GOLD':
    desconto = faturamento_anual * 0.1

elif assin.upper() == 'PLATINUM':
    desconto = faturamento_anual * 0.05

print('\n{}, você faturou R${} e terá que pagar R${}!'.format(nome, faturamento_anual, desconto))

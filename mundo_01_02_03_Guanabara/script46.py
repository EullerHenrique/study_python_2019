valor_da_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao_mensal = valor_da_casa / (anos*12)
minimo = ((30/100)*salario)
print('Para pagar uma casa de R${:.2F} em {} anos'.format(valor_da_casa,anos), end= '')
print(' a prestação será de R${:.2f}'.format(prestacao_mensal))

if prestacao_mensal > minimo:
    print('Empréstimo negado')
else:
    print('Emprésitimo concedido')
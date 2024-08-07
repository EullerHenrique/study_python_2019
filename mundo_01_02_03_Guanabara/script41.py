salario = float(input('Qual é o salário do funcionário: '))
if salario <= 1250:
    novo = ((15/100)*salario)+salario
else:
    aumento = ((10/100)*salario)+salario
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario,novo))    
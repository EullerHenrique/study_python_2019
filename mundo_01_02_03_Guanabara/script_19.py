dias = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos km rodados?'))
preco = (60 * dias) + (0.15*km_rodados)
print('O total a pagar é de R${:.2f}'.format(preco))

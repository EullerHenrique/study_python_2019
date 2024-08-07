distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prester a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
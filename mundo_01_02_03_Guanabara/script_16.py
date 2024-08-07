preco = float(input('Digite o preço do produto: '))
desconto = (5/100) * preco #ou (preco * 5)/100
print('O preço com 5 % de desconto é {}'.format(preco - desconto))
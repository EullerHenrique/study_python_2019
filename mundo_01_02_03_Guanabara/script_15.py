largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parade? '))
area = largura * altura
qtd_tinta = area/2

print('A area da parede é {} m2'.format(area))
print('A quantidade de tinta para pintar a parede é {} litros'.format(qtd_tinta))
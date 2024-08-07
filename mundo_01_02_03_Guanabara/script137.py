def ficha(j = 'Desconhecido',g=0):
    print(f'O jogador {j} fez {g} gol(s) no campeonato')


j = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(g=g)
else:
    ficha(j,g)

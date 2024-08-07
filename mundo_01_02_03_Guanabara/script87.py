times = ('Corinthians','Palmeiras','Santos','Grêmio',
          'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
          'Atlético','Botafogo','Atlético-PR','Bahia',
          'São Paulo', 'Fluminense','Sport Recife',
          'FC Vítoria', 'Coritiba','Avaí','Ponte Preta',
          'Atlético-GO')

print('-='*15)
print('Lista de times: {times}')
print('-='*15)

#for t in times:
#    print(t)

print(f'OS 5 primeiros são {times[0:5]}')
print('-='*15)

print(f'Os 4 últimos são {times[-4:]}')
print('-='*15)

print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)

print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')
print('-='*15)


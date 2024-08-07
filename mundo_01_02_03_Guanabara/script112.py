dados = dict()
dados = {'Nome':'Pedro','Idade':25}
print(dados['Nome'])
print(dados['Idade'])
dados['Sexo'] = 'M'
del dados['Idade']

filme = dict()
filme = {'Titulo':'Star Wars', 'Ano':1977,
         'Diretor':'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')


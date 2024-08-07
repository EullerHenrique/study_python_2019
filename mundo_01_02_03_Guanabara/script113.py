pessoas = {'nome':'Euller','sexo':'M','idade':19}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
pessoas['nome']= 'carol'
pessoas['peso'] = 35

for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')

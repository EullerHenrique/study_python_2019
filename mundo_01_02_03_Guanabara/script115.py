estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    #Quando n se usa dicionário não pode copiar desse jeito
    #brasil.append(estado[:])

    #Jeito Correto
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')
for e in brasil:
    for v in e.values():
        print(v,end=' ')
    print()
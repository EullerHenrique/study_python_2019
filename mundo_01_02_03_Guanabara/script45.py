nome = str(input('Qual é o seu nome? '))
if nome == 'Euller':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudio Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem comum. ')

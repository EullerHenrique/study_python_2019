print('='*30)
print('{:^30}'.format('BANCO NUBANK'))
print('='*30)
valor = int(input('Que valor você quer sacar?: R$'))
total = valor
cedula = 50
totalced = 0
while True:
    if total >= cedula:
        total = total - cedula
        totalced = totalced + 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO NUBANK! Tenha um bom dia!')        
        
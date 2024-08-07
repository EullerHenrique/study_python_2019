from time import sleep


def maior(*num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end = '', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        cont += 1
    print()
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    print()








maior(2,9,4,5,7,1)
maior(4,7,8)
maior(1,2)
maior(6)
maior()
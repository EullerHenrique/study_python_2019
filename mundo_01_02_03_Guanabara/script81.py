from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}, ',end='')
    
    if total % 2 == 0:
        print('Deu par ')
    else:
        print('Deu ímpar ')
    
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v = v + 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você venceu!')
            v = v + 1 
        else:
            print('Você perdeu!')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
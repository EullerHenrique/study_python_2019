import random
import time

itens = ('Pedra','Papel','Tesoura')
computador = random.randint(0,2)
print('''Suas opções:
0 - Pedra
1 - Papel
2 - Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
if jogador > 2:
    print('Jogada inválida')
else:
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    time.sleep(1)
    
    print('-='*11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-='*11)

    if computador == 0:
        if jogador == 0:
            print('Empate')
        elif jogador == 1:
            print('Jogador vence')
        elif jogador == 2:
            print('Computador vence')
    elif computador == 1:
        if jogador == 0:
            print('Computador vence')
        elif jogador == 1:
            print('Empate')
        elif jogador == 2:
            print('Jogador vence')
    elif computador == 2:
        if jogador == 0:
            print('Jogador vence')
        elif jogador == 1:
            print('Computador vence')
        elif jogador == 2:
            print('Empate')
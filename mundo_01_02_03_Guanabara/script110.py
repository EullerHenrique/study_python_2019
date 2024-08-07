from random import randint
from time import sleep

lista  = list()
jogos  = list()
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
quant = int(input('Quantos jogos voçê quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while cont <= 6:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'Sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, 'Boa Sorte','-='*5)
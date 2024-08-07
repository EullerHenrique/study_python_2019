import random
import time
numero_1 = random.randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
numero_2 = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(3)
if numero_2 == numero_1:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}:'.format(numero_1,numero_2))
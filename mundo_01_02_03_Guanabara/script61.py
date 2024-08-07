soma  = 0
cont = 0
for i in range(0,6):
    numero = int(input('Digite um número par: '))
    if numero % 2 == 0:
        soma = soma + numero
        cont = cont + 1
print('Você informou {} número pares e a soma foi {}'.format(cont,soma))

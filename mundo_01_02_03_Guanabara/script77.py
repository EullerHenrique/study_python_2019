resp = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma/quant
print('Você digitou {} números e a média foi {}'.format(quant,media))
print('O maior valor foi de {} e o menor foi {}'.format(maior,menor))
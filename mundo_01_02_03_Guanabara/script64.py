frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

#for letra in range(len(junto)-1,-1,-1):
#    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if junto == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
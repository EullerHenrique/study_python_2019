n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end = '')
while c > 0:
    print('{}'.format(c),end = '')
    if c > 1:
        print(' x ',end='')
    else:
        print(' = ',end='')
    f = f * c
    c = c -1
print('{}'.format(f))


numero  = int(input('Que número você deseja converter? '))

print('Escolha uma opção: ')
print('--'*20)
print('1 - Converter para binário')
print('2 - Converter para octal')
print('3 - Converter para hexadecimal')
print('--'*20)

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(numero,bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(numero,oct(numero)[2:]))
elif opcao == 3:
    print('{} convetido para hexadecimal é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('Opção inválida! Tente novamente')


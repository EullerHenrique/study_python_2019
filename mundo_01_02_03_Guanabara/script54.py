print('===== LOJAS EULLER =====')
preco = float(input('Preço das compras: R$'))
print('''Formas de pagamento
1 - à vista dinheiro/cheque
2 - à vista cartão 
3 - 2x cartão
4 - 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (10/100)*preco
elif opcao == 2:
    total = preco - (5/100)*preco
elif opcao == 3:
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (20/100)*preco
    totparc = int(input('Quantas parcelas? '))
    if totparc >= 3:
        parcela = total/totparc
        print('Sua compra será parcelada em {}x de {:.2f} com juros'.format(totparc,parcela))
    else:
        print('O número de parcelas minimo nesta opção de pagamento é 3')
        flag = 1
else:
    total = preco
    print('Opção inválida de pagamento. Tente novamente!')
if flag == 0:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,total))

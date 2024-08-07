import script143_2

p = float(input('Digite o preço: R$'))
print(f'A metade de {script143_2.moeda(p)} é {script143_2.moeda(script143_2.metade(p))}')
print(f'O dobro de {script143_2.moeda(p)} é {script143_2.moeda(script143_2.dobro(p))}')
print(f'Aumentando 10% temos R${script143_2.moeda(script143_2.aumentar(p,10))}')
print(f'Diminuindo 10% temos R${script143_2.moeda(script143_2.diminuir(p,10))}')

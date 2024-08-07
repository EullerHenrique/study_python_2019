def aumentar(p = 0, t = 0, formato = False):
    res = p + (p*t/100)
    return res if formato == False else moeda(res)

def diminuir(p = 0, t = 0, formato = False):
    res = p - (p*t/100)
    return res if formato == False else moeda(res)

def dobro(p = 0, formato = False):
    res = p*2
    return res if formato == False else moeda(res)

def metade(p = 0, formato = False):
    res = p/2
    return res if formato == False else moeda(res)

def moeda(p = 0, m = 'R$'):
    return f'{m}{p:>.2f}'.replace('.',',')

def resumo(p = 0, tA = 10, tD = 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{tA}% de aumento: \t{aumentar(p,tA,True)}')
    print(f'{tD}% de redução: \t{diminuir(p,tD,True)}')
    print('-'*30)
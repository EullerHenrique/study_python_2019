def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função pelo Euller - BSI-UFU-TERCEIRO PERIODO-2019-2
    """
    c = i
    while c <= f:
        print(f'{c} ', end = '')
        c += p
    print('FIM')

help(contador)
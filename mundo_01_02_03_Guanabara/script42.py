import datetime
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    #Para ser bissexto deve acontecer um dos casos:
    #- se o resto da divisão do ano por 4 for 0, o resto da divisão por 100 não pode ser 0.
    #- se o resto da divisão por 4 não for 0, o resto da divisão por 400 deve ser 0.
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
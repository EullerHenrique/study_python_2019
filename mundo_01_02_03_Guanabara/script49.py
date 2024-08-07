import datetime
ano_de_nascimento = int(input('Em que ano você nasceu? '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_de_nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(ano_de_nascimento,idade,ano_atual))
if idade < 18:
    print('Você deve se alistar no serviço militar daqui {} ano(s), em {}'.format(18 - idade, (ano_atual + (18 - idade))))
elif idade == 18:
    print('Já é hora de se alistar')
else:
    print('Você deveria ter se alistado há {} ano(s) atrás, em {}'.format(idade - 18, ano_atual - (idade - 18)))
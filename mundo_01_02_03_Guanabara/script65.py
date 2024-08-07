import datetime
ano_atual = datetime.date.today().year
idade = 0
maior_idade = 0
menor_idade = 0
for i in range(1,8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    idade = ano_atual - nascimento
    if idade >= 18:
        maior_idade = maior_idade + 1
    else:
        menor_idade = menor_idade + 1
print('Há {} pessoas maiores de idade'.format(maior_idade)) 
print('Há {} pessoas menores de idade'.format(menor_idade))   

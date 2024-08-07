import random
aluno_1 = str(input('Digite o nome do primeiro aluno: '))
aluno_2 = str(input('Digite o nome do segundo aluno: '))
aluno_3 = str(input('Digite o nome do terceiro aluno: '))
aluno_4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))
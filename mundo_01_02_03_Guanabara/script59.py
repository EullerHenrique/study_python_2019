# s = 0
#cont = 0
# for i in range(1,501):
#    if i % 2 != 0 and i % 3 == 0:
#        cont = cont + 1
#        s = s + i
#print('A soma de todos os {} valores solicitados é {}'.format(cont,s))

#ou

soma = 0
cont = 0
for i in range(1,501,2):
    if i % 3 == 0:
        cont = cont + 1
        soma = soma + i
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))


        
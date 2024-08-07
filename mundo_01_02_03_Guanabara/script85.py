lanche = ('Hamburguer','Suco','Pizza','Pudim')
#print(lanche[2:])
#print(lanche)
#print([-2])
#Tuplas são imutáveis
# lanche[1] = "Refri" - erro

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
   print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
    print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print('teste')
print(c.index(5,1))

pessoa = ('Gustavo', 39,'M', 99.88)
del(pessoa[0]) #gera erro, n se pode apagar um elemento de uma tupla e usa-lá depois
print(pessoa)


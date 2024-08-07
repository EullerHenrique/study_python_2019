numero = str(input('Digite um número: '))
divisão = numero.split()
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]
print("""
Unidade {}
Dezena = {}
Centena = {}
Milhar = {}""".format(unidade,dezena,centena,milhar))

#ou
#unidade = numero // 1 % 10
#dezena = numero // 10 % 10
#centenca = numero // 100 % 10
#milhar = numero // 1000 % 10
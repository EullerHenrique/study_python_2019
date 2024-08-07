nome  = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print(
"""
Muito prazer em te conhecer
Seu primeiro nome é {}
Seu último nome é {}
""".format(separa[0], separa[len(separa)-1]))
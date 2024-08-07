def soma(x,y):
    print(f'X ={x} e Y = {y}')
    s = x + y
    print(f'A soma X e Y = {s}')

#soma(1,2)
#soma(x=2,y=3)

#Empacotamento de parametros
#*num = desempacotar paramentros
def contador(*num):
    for valor in num:
        print(valor, end = ' ')
    print()
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam}')

#contador(5,7,3,1,4)
#contador(8,4,7)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos+= 1

valores = [6,3,9,1,8,2]
dobra(valores)
print(valores)
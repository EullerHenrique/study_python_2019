def funcao():
    #váriavel local
    #n1 = 4
    #print(f'n1 dentro vale {n1}')
    
    #variável global   
    global n1
    n1 = 4
    print(f'n1 dentro vale {n1}')


n1 = 2
funcao()
print(f'n1 fora vale {n1}')
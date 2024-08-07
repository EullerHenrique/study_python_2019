num = [2,4,9,1]
num[2] = 3
#num[4] = 7
num.append(7)
num.sort()
num.insert(2,2)
#num.pop(2)
num.remove(2)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')


print(num)
num.sort(reverse=True)
print(num)

print(f'Essa lista tem {len(num)} elementos')
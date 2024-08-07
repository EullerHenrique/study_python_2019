# co = float(input('Digite o comprimento do cateto oposto: '))
# ca = float(input('Digite o comprimento do cateto adjacente: '))
# hip = (ca**2 + co**2) ** (1/2)
# print('O comprimento da hipotenusa é {:.2f}'.format(hip))

#ou

import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))
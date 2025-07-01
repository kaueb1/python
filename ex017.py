from math import hypot
co = float(input('Compriemnto do cateto oposto: '))
ca = float(input('Compriemnto do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
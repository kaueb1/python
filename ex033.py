a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#verificando quem é menor1
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#verificando quem é maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
aa
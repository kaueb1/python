núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print('{} '.format(c), end='')
print('O número {} foi dividido {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
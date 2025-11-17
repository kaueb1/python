from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(randint(n))
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('pronto!')



#def somaPar()

números = list()
sorteia(números)
print(números)

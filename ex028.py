
from random import randint
from time import sleep

computador = randint(0, 5) #faz o pc pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar.')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Processando...')
    sleep(2)
    print('Parabéns, você conseguiu me vencer!')
else:
    print('Processando...')
    sleep(2)
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))

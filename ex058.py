from random import randint
computador = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número de 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Acertou com {} palpites'.format(palpites))
.
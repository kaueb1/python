sal = float(input('Digite o salário do funcionário: '))
if sal <= 1250:
    novosal = sal*1.15
else:
    novosal = sal*1.10
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal, novosal))
vel = float(input('Qual é a velocidade de um carro?: '))
multa = (vel - 80) * 7
if vel > 80:
    print('MULTADO! Você exedeu o limite permitido, que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia, dirija com segurança')

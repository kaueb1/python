distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de {:.2f} reais'.format(preço))
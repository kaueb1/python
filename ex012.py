preço = float(input('Qual é o preço do produto? RS$'))
novo = preço - (preço * 5/ 100)
print('O produto que custava RS${}, na promoção com desconto de 5% vai custar RS${}'.format(preço, novo))

from datetime  import date
ano = float(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {:.0f} é BISSEXTO'.format(ano))
else:
    print('O ano {:.0f} NÃO é BISSEXTO'.format(ano))
2
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano a pessoa nasceu'.))
idade = atual - nasc
if idade >= 21:
    print('Essa pessoa é maior')
else: print('Essa pessoa é menor')
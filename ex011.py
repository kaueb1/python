larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print("Sua parede tem a dimensão de {} x {} e sua área é de {} metros quadrados.".format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))

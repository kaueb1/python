times = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Mirassol', 'Botafogo',
         'Bahia', 'São Paulo', 'Fluminense', 'Bragantino', 'Gremio',
         'Vasco', 'Corinthians', 'Ceará', 'Atlético Mineiro', 'Internacional',
         'Santos', 'Juventude', 'Vitória', 'Fortaleza', 'Recife')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[16:20]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Palmeiras está na {times.index("Palmeiras")+1} posição')
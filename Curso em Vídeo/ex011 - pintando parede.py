lar = float(input('Qual é a largura da parede? '))
alt = float(input('Qual é a altura da parede? '))
area = lar * alt
tin = area / 2
print('A área de uma parede de dimensões ',lar,' x ',alt,' tem área igual a {:.2f}m, precisará de {:.2f} litros de tinta'.format(area,tin), ' para ser pintada')

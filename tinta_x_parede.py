lar = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = lar * alt
print('Sua parede tem {}x{}, e sua área é de {}m².'.format(lar, alt, area))
tinta= area / 2
print('Para pintar essa parede você vai precisr de {} litros de tinta'.format(tinta))
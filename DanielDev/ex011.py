print('WallColor Calculator')
print('')
p1 = float(input('Qual é a altura da parede? '))
p2 = float(input('E a largura? '))
area = str(p1 * p2)
print(f'Sua parede tem a dimensão de {p1}x{p2} e a sua area: {area}m²')
print(f'Para pintar essa parede, você vai precisar de {p2*(p1/2)}L de tinta.')


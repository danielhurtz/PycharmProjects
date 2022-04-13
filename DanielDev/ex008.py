print('Seja bem vindo ao M Calculator')
print('')
medida = float(input('Para iniciar digite uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'Essa medida de {medida}m corresponde a {cm:.0f}cm e {mm:.0f}mm.')
print('Fim.')
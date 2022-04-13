print('')
print('Wallet BRL-USD-EUR Converter')
print('')
print('-'*75)
print(' * Cotação atual: Dolar $1,00 - R$5,27  Euro €1,00 - R$6,02        fev/2022')
print('-'*75)
print('')
real = float(input('Quanto você tem na carteira? R$'))
print('')
dol = 5.27
eur = 6.02
Dolar = real / dol
Euro = real / eur
print(f'Com R${real:.2f} reais você pode comprar ${Dolar:.2f} dólares.')
print(f'Com R${real:.2f} reais você pode comprar €{Euro:.2f} euros.')
print('')
print(':)')



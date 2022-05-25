# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela sia porcao inteira.
# from math import trunc
import math
num = float(input('Digite um numero: '))
inte = math.trunc(num)
print(f'O numero {num} tem a parte inteira {inte}')

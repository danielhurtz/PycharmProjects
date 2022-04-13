num = int(input('Digite um número para saber sua tabuada: '))

print('A tabuada de {} é: '.format(num))

a = 0

for i in range(1,11):
    a = a+1
    print('{} x {} = ' .format(num,a), num*i)

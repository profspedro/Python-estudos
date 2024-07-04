'''enuniado: Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
from math import factorial
num = int(input('Digite um número para calcular o seu fatorial: '))
fat = factorial(num)
cont = num
print('Calculando {}! = '.format(num),end='')
while cont > 0:
    print('{}'.format(cont),end='')
    print(' x ' if cont > 1 else ' = ',end='')
    cont -= 1
print('{}'.format(fat))

#print('O fatorial de {} é {}'.format(num,fat))

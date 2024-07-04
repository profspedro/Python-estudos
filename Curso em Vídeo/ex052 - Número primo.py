'''enunciado: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
div = 0
num = int(input('Qual número você quer saber se é número primo? '))
for cont in range (1,num+1):
    if num % cont == 0:
        div += 1
        print('\033[31m', end='')
    else:
        print('\033[34m',end='')
    print('{} '.format(cont),end='')
if div == 2:
    print('O número {} tem {} divisores, portanto, é PRIMO.'.format(num,div))
elif div != 2:
    print('\n\033[mO número {} tem {} divisores, portanto, NÃO É PRIMO.'.format(num,div))

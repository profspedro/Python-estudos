'''enunciado: Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. No final, mostre os 10 primeiros
termos.'''
from time import sleep
print('-='*30)
print('='*17,' PROGRESSÃO ARITMÉTICA ','='*17)
print('-='*30)
a1 = int(input('Qual o primeiro termo da PA? '))
raz = int(input('Qual a razão da PA? '))
a10 = a1 + 9*raz
print('Processando... ')
sleep(1)
for c in range (a1,a10 + raz,raz):
    print(c,end=' / ')


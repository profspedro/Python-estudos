'''enunciado: Faça um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artifício, indo de 10 até 0, com pausa de 1 segundo entre eles.'''
from time import sleep
print('Prepare-se para a contagem regressiva para os fogos de artifício: ')
for c in range (10,-1,-1):
    print(c)
    sleep(1)
print('BUMM! ! !  POOWWW! ! POWWW! ! !')

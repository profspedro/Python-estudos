'''enunciado: Crie um programa que mostre na tela todos os números pares que estão no
intervalo entre 1 e 50.'''
from time import sleep
print('Números pares de 0 a 50:')
for cont in range (0,51,2):
    sleep(0.5)
    print(cont,end=' ')
print('FIM!')

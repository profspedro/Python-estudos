'''enunciado: Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa
deeverá escrever na tela se o usuário venceu ou se perdeu.'''
from random import randint
from time import sleep
escolhido = randint(1,10) #faz o computador sortear um número entre 1 e 10
print('-=-' *20)
valor = int(input('Tente adivinhar um número entre 1 e 10: ')) #Jogador tenta adivinhar
print('-=-' *20)
print('PROCESSANDO...')
sleep(2)
if valor == escolhido:
    print('Você acertou')
else:
    print('Você perdeu. O número pensado foi {}'.format(escolhido))

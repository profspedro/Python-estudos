'''enunciado: Crie um programa que faça o computador jogar jokenpô com você.'''
from random import randint
itens = ('Pedra','Papel','Tesoura')
comp = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jog = int(input('Qual é a sua jogada? '))
print('-='*10)
print('O computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jog]))
print('-='*10)
if comp == 0: #computador jogou PEDRA
    if jog == 0: #jogador jogou PEDRA
        print('EMPATE')
    elif jog == 1: #jogador jogou PAPEL
        print('Jogador VENCEU')
    elif jog == 2: #jogdor jogou TEOSURA
        print('Computador VENCEU')
    else:
        print('Jogada inválida')
elif comp == 1: #computador jogou PAPEL
    if jog == 0:  # jogador jogou PEDRA
        print('Computador VENCEU')
    elif jog == 1:  # jogador jogou PAPEL
        print('EMPATE')
    elif jog == 2:  # jogdor jogou TEOSURA
        print('Jogador VENCEU')
    else:
        print('Jogada inválida')
elif comp == 2: #computador jogou TESOURA
    if jog == 0:  # jogador jogou PEDRA
        print('Jogador VENCEU')
    elif jog == 1:  # jogador jogou PAPEL
        print('Computador VENCEU')
    elif jog == 2:  # jogdor jogou TEOSURA
        print('EMPATE')
    else:
        print('Jogada inválida')

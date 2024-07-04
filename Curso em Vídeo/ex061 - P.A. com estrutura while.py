'''enunciado: Refaça o desafio 051 lendo o primeiro termo e a razão de uma P.A., mostrando os 10 primeiros
termos da progressão usando a estrutura while.'''
a1 = int(input('Qual é o primeiro termo da sequência? '))
raz = int(input('Qual é a razão da sequência? '))
termo = a1
cont = 1
while cont <= 10:
    print('(' if cont == 1 else ' ', end='')
    print('{}'.format(termo), end='')
    print('; ' if cont < 10 else ')', end='')
    termo += raz
    cont += 1



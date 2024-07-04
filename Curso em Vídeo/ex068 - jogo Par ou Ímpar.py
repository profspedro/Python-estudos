'''enunciado: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder. Deve mostrar o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
print('-='*50)
print('                                     VAMOS JOGAR PAR OU ÍMPAR')
print('-='*50)
cont = 0
while True:
    jogador = int(input('Digite um valor entre 0 e 5: '))
    comp = randint(0,5)
    soma = jogador + comp
    resuljog = ' '
    while resuljog not in 'PI':
        resuljog = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {comp}. Total de {soma}',end=' -> ')
    print('PAR' if soma % 2 == 0 else 'ÍMPAR')
    print('--' * 50)
    if resuljog == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU !')
            break
    elif resuljog == 'I':
        if soma % 2 == 1:
            print('Você VENCEU')
            cont += 1
        else:
            print('Você PERDEU !')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')

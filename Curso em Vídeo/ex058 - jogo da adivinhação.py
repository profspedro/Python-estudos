'''enunciado: Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número de 0 a 10. Só
que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.

from random import randint
escolhido = randint(1,10) #faz o computador sortear um número entre 1 e 10
print('-='*35)
jogador = int(input('Tente adivinhar o número que o computador sorteou, entre 1 e 10: '))
print('-='*35)
cont = 1
while jogador != escolhido:
    print('Você errou. Tente novamente.')
    jogador = int(input('Qual seu palpite? '))
    cont += 1
print('Você acertou após {} tentativas'.format(cont))'''


from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente um número maior')
        elif jogador > computador:
            print('Menos... Tente um número menor')
print('Acertou após {} tentativas ! ! !'.format(palpites))

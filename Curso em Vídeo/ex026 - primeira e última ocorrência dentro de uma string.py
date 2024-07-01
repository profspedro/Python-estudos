'''enunciado: Faça um programa que lei auma frase pelo teclado e mostre:
Quantas vezes aparece a letra A
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez'''
frase = str(input('Digite uma frase: ')).strip()
print('A primeira letra A está na posição {}'.format(frase.upper().find('A') + 1))
print('A letra A aparece {} vezes na frase'.format(frase.upper().count('A')))
print('A última letra apareceu na posição {}'.format(frase.rfind('A')+1))
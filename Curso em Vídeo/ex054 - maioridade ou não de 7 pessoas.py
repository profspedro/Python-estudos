'''Enunciado: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range (0,7):
    nasc = int(input('Qual ano de nascimento da pessoa? '))
    idade = atual - nasc
    print('A idade da pessoa é {} anos'.format(idade))
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
print('O número de pessoas que já atingiram a maioridade é igual a {}'.format(maior))
print('O número de pessoas que não atingiram a maioridade é igual a {}'.format(menor))

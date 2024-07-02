'''enunciado: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela
uma mensagem:
o primeiro valor é maior
o segundo valor é maior
não existe valor maior, os dois são iguais'''
a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
if a > b:
    print('O primeiro valor, {}, é maior'.format(a))
elif a < b:
    print('O segundo valor, {}, é maior'.format(b))
elif a == b:
    print('Não existe valor maior, os dois são iguais.')

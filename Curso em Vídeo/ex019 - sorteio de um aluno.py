''' enunciado do exercício:
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele a ler o nome dos alunos e escolher um deles.'''
from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))

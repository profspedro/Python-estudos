'''enunciado: Faça um programa que leia três números e mostre qual
é o maior e qual é o menor'''

a1 = int(input('Primeiro valor: '))
a2 = int(input('Segundo valor: '))
a3 = int(input('Terceiro valor: '))
if a1 < a2 and a2 < a3:
    menor = a1
    maior = a3
if a1 < a3 and a3 < a2:
    menor = a1
    maior = a2
if a2 < a1 and a1 < a3:
    menor = a2
    maior = a3
if a2 < a3 and a3 < a1:
    menor = a2
    maior = a1
if a3 < a1 and a1 < a2:
    menor = a3
    maior = a2
if a3 < a2 and a2 < a1:
    menor = a3
    maior = a1
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
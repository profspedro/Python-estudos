'''Enunciado: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e
o menor pesos lidos'''
maior = 0
menor = 0
for c in range (0,5):
    pes = float(input('Qual é o peso a ser considerado? (em kg) '))
    if c == 0:
        maior = pes
        menor = pes
    elif pes > maior:
        maior = pes
    elif pes < menor:
        menor = pes
print('O maior peso classificado foi {} kg'.format(maior))
print('O menor peso classificado foi {} kg'.format(menor))

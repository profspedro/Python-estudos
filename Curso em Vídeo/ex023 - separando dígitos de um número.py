''' enunciado: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
dígitos separados.
Ex.: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
Unid. de milhar: 1'''
valor = int(input('Digite um número: '))
unid = valor // 1 % 10
dez = valor // 10 % 10
cen = valor // 100 % 10
unmil = valor // 1000 % 10
print('Analisando o número {}'.format(valor))
print('Unidade: {}'.format(unid))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Unidade de milhar: {}'.format(unmil))

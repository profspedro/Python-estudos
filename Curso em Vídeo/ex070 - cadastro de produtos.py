'''enunciado: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar. No final, mostre:
a) qual é o total gasto na compra;
b) quantos produtos custam mais de R$ 1000;
c) qual é o nome do produto mais barato.'''

print('--'*50)
print('                 LOJA SUPER BARATÃO')
print('--'*50)
resp = 'S'
while resp == 'S':
    nome = str(input('Nome do produto: '))
    pre = float(input('Preço do produto: '))
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while resp != 'SsNn':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp == 'SsNn':
            break
    if resp == 'S':
        break


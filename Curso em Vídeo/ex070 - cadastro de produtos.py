'''enunciado: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar. No final, mostre:
a) qual é o total gasto na compra;
b) quantos produtos custam mais de R$ 1000;
c) qual é o nome do produto mais barato.'''

tot = tot1000 = menor = cont = 0
barato = ' '
print('--'*50)
print('                              LOJA SUPER BARATÃO')
print('--'*50)
while True:
    nome = str(input('Nome do produto: '))
    pre = float(input('Preço do produto: R$ '))
    cont += 1
    if pre > 0:
        tot += pre
    if pre > 1000:
        tot1000 += 1
    if cont == 1 or pre < menor:
        menor = pre
        barato = nome
    print('--' * 50)
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O valor total da compra foi R$ {tot:.2f}')
print(f'{tot1000} produtos custaram mais de R$ 1000,00')
print(f'O produto mais barato foi {barato}, que custa R$ {menor:.2f}')

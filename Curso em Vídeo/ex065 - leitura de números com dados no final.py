'''enunciado: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valor lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar os valores.'''

resp = 'S'
cont = soma = maior = menor = 0
while resp == 'S':
    num = int(input('Digite um número inteiro: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = (soma)/cont
print('Você digitou {} números.'.format(cont))
print('A média aritmética entre esses números é {:.2f}'.format(media))
print('O maior desses números é {}'.format(maior))
print('O menor desses números é {}'.format(menor))

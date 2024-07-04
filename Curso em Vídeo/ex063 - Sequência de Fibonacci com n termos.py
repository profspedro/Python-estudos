'''enunciado: Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma sequência de Fibonacci.'''

print('-'*50)
print('         Sequência de Finacci')
print('-'*50)
lim = int(input('Quantos termos quer visualizar? '))
t1 = 0
t2 = 1
print('~'*50)
print('{}, {}'.format(t1,t2),end='')
cont = 3
while cont <= lim:
    t3 = t1 + t2
    print(', {}'.format(t3),end='')
    cont += 1
    t1 = t2
    t2 = t3
print('\n')
print('~'*50)

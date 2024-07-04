'''enunciado: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

print('-='*50)
print('Tabuada de Números Inteiros positivos')
print('-='*50)
print('Se digitar um número negativo, o programa será interrompido.')
while True:
    num = int(input('\nQual o número cuja tabuada de multiplicação você quer visualizar o resultado? '))
    if num < 0:
        break
    for cont in range (1,11):
        prod = num * cont
        print(f'{num} x {cont} = {prod}')
print('\nTabuada apresentada com sucesso.')

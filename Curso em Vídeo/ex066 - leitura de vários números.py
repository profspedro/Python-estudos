'''enunciado: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valo 999, que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles.'''

num = soma = cont = 0
while True:
    num = int(input('Digite um número: [999 para parar] '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores digitados é igual a {soma}')

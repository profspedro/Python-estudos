'''enunciado: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500'''
soma = 0
cont = 0
for c in range (1,501):
    if c % 3 == 0 and c % 2 != 0:
        #print(c,end=' ')
        cont += 1
        soma += c
print('A soma dos {} múltiplos de 3, que são ímpares, no intervalo entre 1 e 500 é {}'.format(cont,soma))

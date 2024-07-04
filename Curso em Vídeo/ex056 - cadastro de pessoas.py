'''Enunciado: Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
No final do programa, mostre:
- a média da idade do grupo
- qual é o nome do homem mais velho
- quantas mulheres tem menos de 20 anos'''
somaid = 0
mediaid = 0
maioridhom = 0
nomevel = ''
totmulher20 = 0
for cont in range (1,5):
    print('-'*5,cont,'a. PESSOA','-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaid += idade
    if cont == 1 and sexo in 'Mm':
        maioridhom = idade
        nomevel = nome
    if sexo in 'Mm' and idade > maioridhom:
        maioridhom = idade
        nomevel = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaid = (somaid)/4
print('A média de idade do grupo é de {} anos.'.format(mediaid))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridhom,nomevel))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))


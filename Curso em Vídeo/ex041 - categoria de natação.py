'''enunciado: A confederação nacional de natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 20 anos: SÊNIOR
- acima de 20 anos: MASTER'''
from datetime import date
nasc = int(input('Qual o ano de nascimento? '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Tem {} anos e vai praticar natação na categoria MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('Tem {} anos e vai praticar natação na categoria INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('Tem {} anos e vai praticar natação na categoria JUNIOR'.format(idade))
elif 19 < idade <= 20:
    print('Tem {} anos e vai praticar natação na categoria SÊNIOR'.format(idade))
elif idade > 20:
    print('Tem {} anos e vai praticar natação na categoria MASTER'.format(idade))


'''enunciado: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade:
- se ele ainda vai se alistar ao serviço militar.
- se é a hora de se alistar.
- se já passou o tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''
from datetime import date
nasc = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - nasc
if idade < 18:
    print('Você tem {} anos. Faltam {} para o alistamento militar.'.format(idade,(nasc + 18 - atual)))
    alist = nasc + 18
    print('Seu alistamento militar deverá ser no ano {}'.format(alist))
elif idade == 18:
    print('Está na hora de fazer o alistamento militar. CORRA!')
elif idade > 18:
    saldo = idade - 18
    print('Você tem {} anos. Deveria ter se alistado há {} anos.'.format(idade,saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))



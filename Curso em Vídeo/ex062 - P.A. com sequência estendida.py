'''enunciado: Melhore o desafio 061 perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.

a1 = int(input('Qual é o primeiro termo da sequência? '))
raz = int(input('Qual é a razão da sequência? '))
n = int(input('Quantos termos quer nessa P.A.? '))
termo = a1
cont = 1
while cont <= n:
    print('(' if cont == 1 else ' ', end='')
    print('{}'.format(termo), end='')
    print('; ' if cont < n else ')', end='')
    termo += raz
    cont += 1

(o programa acima não corresponde ao que o enunciado pede, porém, é muito eficiente também.'''

a1 = int(input('Qual é o primeiro termo da sequência? '))
raz = int(input('Qual é a razão da sequência? '))
termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('(' if cont == 1 else ' ', end='')
        print('{}'.format(termo), end='')
        print('; ' if cont < total else '; ...)', end='')
        termo += raz
        cont += 1
    print(' PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão Aritmética finalizada com {} termos mostrados.'.format(total))

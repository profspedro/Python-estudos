'''enunciado: Crie um programa que leia dois valores e mostre um menu na tela:
[1] adição
[2] multiplicação
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Primeiro número inteiro: '))
n2 = int(input('Segundo número inteiro: '))
op = 0
while op != 5:
    print('-=-'*20)
    print('''    [1] Adição
    [2] Multiplicação
    [3] maior
    [4] Novos números
    [5] Sair do programa''')
    op = int(input('Qual é a sua opção? '))
    print('-=-'*20)
    if op == 1:
        print('A soma dos números {} e {} é igual a {}'.format(n1,n2,(n1 + n2)))
    elif op == 2:
        print('A multiplicação dos números {} e {} é igual a {}'.format(n1,n2,(n1 * n2)))
    elif op ==3:
        if n1 < n2:
            print('O maior número é {}'.format(n2))
        else:
            print('O maior número é {}'.format(n1))
    elif op == 4:
        print('Informe os números novamente. ')
        n1 = int(input('Primerio valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa. Volte sempre! ! !')

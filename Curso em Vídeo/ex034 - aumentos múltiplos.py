'''enunciado: Escreva um programa que pergunte o salário
de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1250.00, calcule um
aumento de 10%. Para compras inferiores ou iguais a esse
valor, o aumento é de 15%'''

sal = float(input('Qual é o salário do funcionário? R$ '))
if sal > 1250:
    nsal = sal * 1.1
    print('O salário do funcionário era R$ {} e agora, após um aumento de 10%, passou a ser R$ {}'.format(sal,nsal))
if sal <= 1250:
    nsal = sal * 1.15
    print('O salário do funcionário era R$ {} e agora, após um aumento de 15%, passou a ser R$ {}'.format(sal, nsal))

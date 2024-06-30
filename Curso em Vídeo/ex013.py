sal = float(input('Qual o salário do funcionário? R$ '))
aum = sal*15/100
nsal = sal + aum
print('O funcionário teve um aumento de 15%, isto é, de R$ {}, e agora o novo salário dele é R$ {}'.format(aum, nsal))

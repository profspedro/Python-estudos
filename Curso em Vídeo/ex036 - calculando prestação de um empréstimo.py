'''enunciado: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
empréstimo será negado.'''
print('-=-'*30)
print(' '*33,'EMPRÉSTIMO BANCÁRIO')
print('-=-'*30)
casa = float(input('Qual o valor total do empréstimo que precisa para a aquisição do imóvel? R$ '))
sal = float(input('Qual o seu salário? R$ '))
tem = int(input('Em quantos anos pretende pagar? '))
pres = casa / (tem * 12)
psal = sal * 0.3
if pres > psal:
    print('Sinto muito! Seu empréstimo foi negado.')
else:
    print('Seu empréstimo foi aprovado. O valor da prestação mensal que você pagará é R$ {:.2f}'.format(pres))

'''enunciado: Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal
e condição de pagamento:
- à vista: dinheiro/cheque: 10% de desconto;
- à vista no cartão: 5% de desconto;
- em até 2x no cartão: preço normal;
- 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format('LOJAS TUDO DO BOM E DO MELHOR'))
pre = float(input('Qual o preço das compras? R$ '))
print('''Qual a forma de pagamento?
[1] à visga dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais''')
fin = int(input('Qual é a opção? '))
if fin == 1:
    tot = pre * 0.9
elif fin == 2:
    tot = pre * 0.95
elif fin == 3:
    tot = pre
    print('O valor de cada uma das 2 parcelas será de R$ {:.2f} '.format(tot/2))
elif fin == 4:
    tot = pre * 1.2
    parc = int(input('Em quantas parcelas deseja pagar? '))
    print('O valor de cada uma das parcelas será R$ {}'.format(tot/parc))
print('Sua compra de R$ {} vai custar R$ {:.2f} no final'.format(pre,tot))

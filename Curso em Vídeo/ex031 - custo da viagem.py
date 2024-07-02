'''enunciado: Desenvolva um programa que pergunte a distância de uma viagem, em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km
e R$ 0,45 para viagens mais longas.'''

dist = float(input('Qual a distância a ser percorrida nessa viagem? (em Km) '))
if dist <= 200:
    print('O valor de sua passagem é R$ {:.2f}'.format(dist * 0.50))
else:
    print('O valor de sua passagem é R$ {:.2f}'.format(dist * 0.45))

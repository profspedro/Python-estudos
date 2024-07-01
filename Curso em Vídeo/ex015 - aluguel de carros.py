dist = float(input('Qual a distância percorrida? (em Km) '))
dias = int(input('Quantos dias de aluguel? '))
preco = dist*0.15 + dias*60
print('O total a pagar é de R$ {:.2f}'.format(preco))

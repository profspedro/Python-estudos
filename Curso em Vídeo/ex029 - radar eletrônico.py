'''enunciado: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite.'''

vel = float(input('Qual a velocidade do automóvel? (em km/h) '))
if vel <= 80:
    print('Dirija com cuidado! Todo cuidado é pouco no trânsito.')
else:
    print('<<<MULTADO>>> O valor da sua multa é R$ {:.2f}'.format((vel - 80)*7))

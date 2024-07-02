nome = str(input('Qual é seu nome? '))
if nome == 'Pedro':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(media))
print('PARABÉNS!' if media >= 6 else 'ESTUDE MAIS!')


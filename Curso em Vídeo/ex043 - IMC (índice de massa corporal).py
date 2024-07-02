'''enunciado: Desenvolvendo uma lógica que leia o peso e altura de uma pessoa, calcule seu
IMC e mostre seu status, de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- entre 25 e 30: sobrepeso
- de 30 a 40: obesidade
- acima de 40: obesidade mórbida'''
massa = float(input('Qual a massa corporal? (em kg) '))
alt = float(input('Qual a altura? (em m) '))
imc = (massa)/(alt ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Está ABAIXO DO PESO')
elif 18.5 < imc <= 25:
    print('PARABÉNS! Você está na faixa de PESO IDEAL')
elif 25 < imc < 30:
    print('Está com SOBREPESO')
elif 30 <= imc <= 40:
    print('Está com OBESIDADE')
elif imc > 40:
    print('Está com OBESIDADE MÓRBIDA. Se cuide com urgência!')
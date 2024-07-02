'''enunciado: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: REPROVADO
- média entre 5.0 e 6.9: RECUPERAÇÃO
- média 7,0 ou superior: APROVADO'''
n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
media = (n1 + n2)/2
print('Como as notas foram {} e {}, a média ficou igual a {:.2f}'.format(n1,n2,media))
if media < 5:
    print('O aluno está REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('O aluno está em RECUPERAÇÃO')
elif media >= 7:
    print('O aluno está APROVADO')

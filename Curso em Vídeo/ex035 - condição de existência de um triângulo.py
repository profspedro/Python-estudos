'''enunciado: Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou não formar
um triângulo.'''
print('-=-'*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*20)
a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível construir um triângulo com essas três medidas')
else:
    print('Não é possível construir um triângulo com essas três medidas')

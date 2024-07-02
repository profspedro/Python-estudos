'''enunciado: Refaça o desafio 035 dos triângulos acrescentando o recurso de mostrar que tipo
de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓCELES: dois lados iguais
- ESCALENO: todos os lados diferentes'''
a = float(input('Digite um dos lados do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if a < b + c and b < a + c and c < a + b:
    print('O triângulo de lados {}, {} e {} tem classificação'.format(a, b, c), end=' ')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b and b != c:
        print('ISÓSCELES')
    elif a != b and b != c:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO')



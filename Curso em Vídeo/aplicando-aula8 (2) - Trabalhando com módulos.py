from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, raiz))
print('A raiz quadrada de {} é igual a {}'.format(num, ceil(raiz)))
print('A raiz quadrada de {} é igual a {}'.format(num, floor(raiz)))
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))

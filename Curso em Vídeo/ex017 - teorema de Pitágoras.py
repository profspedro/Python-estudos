'''catop = float(input('Qual é o cateto oposto? '))
catadj = float(input('Qual é o cateto adjacente? '))
hip = (catop ** 2 + catadj ** 2) ** (1/2)
print('O valor da hipotenusa desse triângulo retângulo é ', hip) '''

from math import hypot
catop = float(input('Qual é o cateto oposto? '))
catadj = float(input('Qual é o cateto adjacente? '))
hip = hypot(catop, catadj)
print('O valor da hipotenusa desse triângulo retângulo é ', hip)

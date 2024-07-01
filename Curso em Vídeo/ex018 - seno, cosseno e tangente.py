from math import sin, cos, tan, radians
ang = float(input('Qual é o ângulo (em graus)? '))
rad = radians(ang)
print('O valor de seno é {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}'.format(sin(rad), cos(rad), tan(rad)))

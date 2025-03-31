from math import sin, cos, tan, radians
a = float(input('Digite o valor do ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('Analisando o ângulo {}, \no seno é {:.2f}, \no cosseno é {:.2f}, \ne a tangente é {:.2f}.'.format(a, s, c, t))

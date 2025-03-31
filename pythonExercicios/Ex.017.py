from math import pow, sqrt
ca = float(input('\033[1mQual o comprimento do cateto adjacente? '))
co = float(input('Qual é o comprimento do cateto oposto? '))
h2 = pow(ca, 2) + pow(co, 2)
h = sqrt(h2)
print('\033[35mSe a² = b² + c², \033[msendo \033[33mb = {} e c = {}, \033[32ma² = {} e o valor da hipotenusa é {:.2f}.'.format(ca, co, h2, h))

from math import hypot
print('A hipotenusa do triângulo citado é igual a {:.2f}'.format(hypot(co, ca)))

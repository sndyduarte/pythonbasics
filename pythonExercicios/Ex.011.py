#Desafio 11
l = float(input('Qual a largura da parede em metros? '))
h = float(input('Qual a altura da parede em metros? '))
a = l * h
t = a / 2
print('A área da parede citada é de {}m², portanto serão necessários {}l de tinta para pintá-la.'.format(a, t))
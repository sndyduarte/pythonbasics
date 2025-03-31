# Desafio 15
d = int(input('Por quantos dias o carro foi alugado? '))
k = float(input('Quantos quilômetros foram rodados? '))
p = ((60 * d) + (0.15 * k))
print('O valor do aluguel será de R${:.2f}.'.format(p))

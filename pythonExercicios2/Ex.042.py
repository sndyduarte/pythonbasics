"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo erá formado:
Equilátero: todos os lados iguais
Isósceles: Dois lados iguais
Escaleno: todos os lados diferentes."""

print('~*' * 13)
print(' ANALISADOR DE TRIÂNGULOS')
print('~*' * 13)
lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('As três retas informadas são capazes de formar um triângulo', end=' ')
    if lado1 != lado2 != lado3 != lado1:
        print('ESCALENO.')
    elif lado1 == lado2 == lado3:
        print('EQUILÁTERO.')
    else:
        print('ISÓSCELES.')
else:
    print('As três retas informadas não podem formar um triângulo.')
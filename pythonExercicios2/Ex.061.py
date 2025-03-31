"""Refaça o exercício 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while."""

n = int(input('Digite o número inicial: '))
r = int(input('Digite a razão da PA: '))
c = 0
print(n)
while c < 9:
    n = n + r
    print(n)
    c += 1

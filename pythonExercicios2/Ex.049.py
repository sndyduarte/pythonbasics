"""Refaça o exercício DESAFIO 09, mostrando a tabuada de um número
que o usuário escolher, só que agora usando um laço for."""

n = int(input('Digite um número inteiro: '))
s = 0
print('A tabuada do número {} é:'.format(n))
for i in range(1, 11):
    s = s + n
    print('{} x {:2} = {}'.format(n, i, s))

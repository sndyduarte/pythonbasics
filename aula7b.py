n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1//n2
e = n1 ** n2
print('A soma entre {} e {} é {}, o produto é {}, e a divisão é {:.3f}.'.format(n1, n2, s, m, d))
print('A divisão inteira é {}, e a potência é {}.'.format(di, e))

n = int(input('Digite um número para calcular seu fatorial: '))
f = 1
for i in range(n, 0, -1):
     print('{}'.format(i), end = ' ')
     print(' x ' if i > 1 else ' = ', end=' ')
     f = f * i
print(f)
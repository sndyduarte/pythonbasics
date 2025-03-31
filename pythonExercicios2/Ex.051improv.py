num = int(input('Digite o primeiro termo da P.A: '))
raz = int(input('Digite a razão da P.A: '))
dec = num + (10 - 1) * raz #regra do enésimo número
for c in range(num, dec, raz):
    print('{}'.format(c), end = ' ')
print('FIM')
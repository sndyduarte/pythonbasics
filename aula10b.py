n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua média é {}.'.format(m))
'''if m >= 6:
    print('Você está na média! Parabéns!')
else:
    print('Sua média está baixa. Estude mais.')'''

print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')

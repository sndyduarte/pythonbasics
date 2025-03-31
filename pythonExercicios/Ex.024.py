cidade = input('Digite o nome da sua cidade: ').strip()
v = cidade.upper().split()
print('Sua cidade começa com a palavra "Santo"? {}'.format('SANTO' in v[0]))
#OU#print(cidade[:5].upper() == 'SANTO')

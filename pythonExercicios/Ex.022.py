nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))
print('Seu nome possui {} letras.'.format(len(nome.replace(" ", ""))))
#OU#print('Seu nome possui {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui {} letras.'.format(len(nome.split()[0])))
#OU#print('Seu primeiro nome posui {} letras.'.format(nome.find(' ')))

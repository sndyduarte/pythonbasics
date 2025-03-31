frase = input('Escreva uma frase: ').strip()
print('Sua frase possui {} letras "a"'.format(frase.count('A') + frase.count('a')))
print('A primeira letra "a" da sua frase aparece na posição {}.'.format(frase.lower().find('a')+1))
print('A última letra "a" da sua frase aparece na posição {}.'.format(frase.lower().rfind('a')+1))

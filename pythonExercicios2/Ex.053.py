frase = str(input('Digite uma frase: ')).upper().strip()
'''palavras = frase.split()
junto = ''.join(palavras)'''
junto = frase.replace(' ','')
inverso = ''
print(junto)
for letra in range(len(junto) -1, -1, -1):
     inverso +=junto[letra]
#ou
#inverso = junto[::-1]
print(inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase informada NÃO é um palíndromo.')

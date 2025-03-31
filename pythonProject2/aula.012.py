#Condições aninhadas: Uma condição dentro da outra

nome = str(input('Qual é o seu nome? '))
if nome == 'Sandy':
    print('Belo nome!')
elif nome == 'Marcos' or nome == 'Mateus':
    print('Deus abençoe seu nome bíblico.')
else:
    print('Prazer em conhecer!')
print('Tenha um bom dia, {}!'.format(nome))

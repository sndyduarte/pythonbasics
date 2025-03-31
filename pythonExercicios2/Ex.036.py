"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado."""

print('\033[1;35mBem vindo ao simulador de financiamento! Forneça as seguintes informações para prosseguir,'
      '\nlembrando que o valor da prestação não deve ultrapassar 30% do valor do salário do comprador.')
casa = float(input('\033[1;33mQual o valor da casa que você quer financiar? '))
salário = float(input('\033[1;33mQual o valor do seu salário? R$ '))
anos = int(input('\033[1;33mEm quantos anos você deseja pagar? \033[m'))
prestação = casa / (12 * anos)
if prestação > (30/100) * salário:
    print('Empréstimo \033[1;31mNEGADO\033[m. O valor da prestação é de R${:.2f} e excede 30% do salário do comprador.'
          .format(prestação))
else:
    print('\033[mSeu empréstimo foi \033[1;32mAPROVADO\033[m! O valor da parcela nestas condições é de R${:.2f}.'
          .format(prestação))
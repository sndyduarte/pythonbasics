"""Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e a condição de pagamento:
-À vista dinheiro/cheque: 10% de desconto
-À vista no cartão: 5% de deconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros."""

print('\033[1;36m{:=^40}\033[m'.format(' LOJAS RATIOFLY '))
compras = float(input('Qual foi o valor em compras na loja? \033[32mR$'))
print('''Escolha uma das formas de pagamento abaixo:
      [ 1 ] À vista no dinheiro ou cheque;
      [ 2 ] À vista no cartão;
      [ 3 ] Em 2x no cartão;
      [ 4 ] Em 3x ou mais no cartão.''')
pagto = input('Digite o número da opção que indica a forma de pagamento desejada: ')
if pagto == '1':
    total = compras - (compras * 10/100)
elif pagto == '2':
    total = compras - (compras * 5/100)
elif pagto == '3':
    total = compras
    parcela = total / 2
    print('Suas compras de R${} serão parceladas em 2x de R${:.2f} SEM JUROS.'.format(compras, parcela))
elif pagto == '4':
    vezes = int(input('Em quantas vezes deseja parcelar suas compras? '))
    total = compras + (compras * 20/100)
    parcela = total / vezes
    print('Suas compras de R${} serão parceladas em {}x de R${:.2f} COM JUROS.'.format(compras, vezes, parcela))
else:
    print('Opção inválida! Tente novamente!')
print('O valor total a ser pago será de R${:.2f}.'.format(total))
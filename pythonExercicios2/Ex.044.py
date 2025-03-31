"""Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e a condição de pagamento:
-À vista dinheiro/cheque: 10% de desconto
-À vista no cartão: 5% de deconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros."""

preco = float(input('Qual o preço do produto? '))
forma = str(input('Qual a forma de pagamento: dinheiro, cheque ou cartão? ')).strip()
forma = forma.lower()
if forma == 'cartão' or forma == 'cartao':
    parcela = int(input('Em quantas vezes será dividido o pagamento? (Se for à vista digite 1): '))
    if parcela == 1:
        pag = preco - (preco * 5/100)
    elif parcela == 2:
        pag = preco
    elif parcela >= 3:
        pag = preco + (preco * 20/100)
elif forma == 'dinheiro' or 'cheque':
    pag = preco - (preco * 10/100)
print(f'O valor total a ser pago pelo produto em {forma} será {pag:.2f}')

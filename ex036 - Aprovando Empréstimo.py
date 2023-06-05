valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento:'))
s = valor / (anos * 12)
ss = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, anos, s))
if s > ss:
    print('Empréstimo NEGADO!!')
else:
    print('Empréstimo ACEITO!!')


print('========== BEM-VINDO ==========')
d = int(input('Quantos dias alugados?:'))
k = float(input('Quantos Km rodados?:'))
s = int(d * 60) + float(k * 0.15)
print('O total a pagar será: R${:.2f}'.format(s))



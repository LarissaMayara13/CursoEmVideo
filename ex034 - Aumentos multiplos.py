from time import sleep
a = float(input('Digite o valor do salário: R$'))
print('PROCESSANDO.....')
sleep(2)
if a > 1250:
    print('O valor do novo salário é de: R${:.2f}'.format((a * 0.1) + a))
else:
    print('O valor do novo salário é de: R${:.2f}'.format((a * 0.15) + a))


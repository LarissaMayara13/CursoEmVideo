print('-=-' * 20, 'PAR OU ÍMPAR', '-=-' * 20)
num1 = int(input('Digite um número:'))
a = (num1 % 2)
if a == 0:
    print('O número {} é Par'.format(num1))
else:
    print('O número {} é ímpar'.format(num1))

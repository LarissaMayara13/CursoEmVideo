num = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
num2 = int(input('Sua opção:'))
if num2 == 1:
    print('O valor binário de {} é: {}'.format(num, bin(num)[2:]))
elif num2 == 2:
    print('O valor OCTAL de {} é: {}'.format(num, oct(num)[2:]))
elif num2 == 3:
    print('O valor HEXADECIMAL de {} é: {}'.format(num, hex(num)[2:]))
else:
    print('ERROR! Escolha uma opção válida!')



# MODO SIMPLICADO DE ALINHAMENTO (3 ' NO COMEÇO):
# print('''Escolha uma das bases para conversão:
# [ 1 ] converter para BINÁRIO
# [ 2 ] converter para OCTAL
# [ 3 ] converter para HEXADECIMAL''')
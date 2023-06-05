frase = str(input('Digite uma frase:')).upper().replace(' ','')
invertida = frase[::-1]
print('O inverso de {} é {}'.format(frase, invertida))
if frase == invertida:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')



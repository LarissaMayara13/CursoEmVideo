a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float = float(input('Terceiro segmento:'))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo.', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo.')
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a > b + c and b > a + c and c > a + b:
    print('Os segmentos acima NÃO PODEM formar um Triângulo.')
elif a == b and a == c:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif a == b or a == c or b == c:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓCELES!')
else:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')

'''num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))
num3 = int(input('Terceiro valor:'))
if num1 < num2 and num1 < num3:
    print('O menor valor digitado foi {}'.format(num1))
if num2 < num1 and num2 < num3:
    print('O menor valor digitado foi {}'.format(num2))
if num3 < num1 and num3 < num2:
    print('O menor valor digitado foi {}'.format(num3))
if num1 > num2 and num1 > num3:
    print('O maior valor digitado foi {}'.format(num1))
if num2 > num1 and num2 > num3:
    print('O maior valor digitado foi {}'.format(num2))
else:
    print('O maior valor digitado foi {}'.format(num3))'''

# código do professor:

a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
# verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
# verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))

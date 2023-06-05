# LAÇOS DE REPETIÇÃO ( PARTE 01):

# for c in range (1, 10):  ======> tradução ======> # laço c no intervalo (1, 10):
#   passo                                           #   passo
# pega                                              # pega

# for c in range (0, 3):   ======> tradução ======> # laço c no intervalo (0, 3):
#   passo                                               passo
#   pula                                                pula
# passo                                             # passo
# pega                                              # pega

# for c in range (0, 3):
#   if moeda:
#       pega
#   passo
#   pula
# passo
# pega

# for c in range (0, 6):
#   print(c)
# print('FIM')
# RESULTADO:
'''
0
1
2
3
4
5
FIM
'''

# for c in range (1, 7):
#   print(c)
# print('FIM')
# RESULTADO:
'''
1
2
3
4
5
6
FIM'''

# for c in range (6, 0, -1) ===== VAI CONTAR PRA TRÁS
#   print(c)
# print('FIM')
# RESULTADO:
'''
6
5
4
3
2
1'''

''' for c in range(0, 7, 2)     # CONTOU DE 0 ATÉ 7 PULANDO DE 2 EM 2 #
        print(c)
    print('FIM')
    RESULTADO:
    0
    2
    4
    6
    FIM'''

'''
n = int(input('Digite um número:'))
for c in range (0, n):
    print(c)
RESULTADO:
Digite um número: 7
0
1
2
3
4
5
6
'''

'''n = int(input('Digite um número:'))
for c in range (0, n + 1):
    print(c)

RESULTADO:

Digite um número: 7
0
1
2
3
4
5
6
7
'''

'''
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:))
for c in range(i, f + 1, p)
    print(c)

RESULTADO:

Início: 2
Fim: 9
Passo: 3
2
5
8
'''

'''
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:))
for c in range(i, f + 1, p)
    print(c)

RESULTADO:

Início: 1
Fim: 100
Passo: 10
1
11
21
31
41
51
61
71
81
91
'''

'''
for c in range(0, 3):
    n = int(input('Digite um valor:))
print('fim')

RESULTADO:

Digite um valor: 2
Digite um valor: 6
Digite um valor: 4
fim
'''

'''
s = 0 
for c in range(0, 4):
    n = int(input('Digite um valor:))
    s +=n   # s = s + n
print('O somatório de todos os valores foi {}'.format(s))

RESULTADO:

Digite um valor: 4
Digite um valor: 2
Digite um valor: 3
Digite um valor: 1
O somatório de todos os valores foi 10.
'''

































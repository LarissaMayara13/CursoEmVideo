import random
from time import sleep

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

opção = int(input('Qual a sua jogada?'))

print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PO!!!')
print('-=' * 20)

a1 = [0, 1, 2]
c1 = random.choice(a1)

if c1 == 0:
    print('Computador jogou PEDRA')
elif c1 == 1:
    print('Computador jogou PAPEL')
elif c1 == 2:
    print('Computador jogou TESOURA')
pass
if opção == 0:
    print('Jogador jogou PEDRA')
elif opção == 1:
    print('Jogador jogou PAPEL')
elif opção == 2:
    print('Jogador jogou TESOURA')
pass
print('-=' * 20)

if opção == 0 and c1 == 0 or opção == 1 and c1 == 1 or opção == 2 and c1 == 2:
    print('EMPATE')
elif opção == 0 and c1 == 2 or opção == 1 and c1 == 0 or opção == 2 and c1 == 1:
    print('JOGADOR VENCE')
else:
    print('COMPUTADOR VENCE')


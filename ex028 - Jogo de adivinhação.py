import random
from time import sleep

print('-=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 30)
a1 = [0,1,2,3,4,5]
c1 = random.choice(a1)
num1 = int(input('Em que número pensei?:'))
print('PROCESSANDO....')
sleep(3)
if c1 == num1:
    print('Você ACERTOU!!')
else:
    print('Você ERROU!! Eu pensei no número {} e não no {}'.format(c1, num1))

"""from random import randint
computador = randint(0, 5) #faz o computador 'pensar'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) # Jogador tenta adivinhar
if jogador == computador:
    print('PARABÉNS! Você consguiu me vender!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(computador, jogador))"""








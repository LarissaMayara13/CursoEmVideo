dis = float(input('Digite a distância em Km da viagem:'))
a1 = (dis * 0.5)
a2 = (dis * 0.45)
if dis <= 200:
    print('O custo da sua viagem será de: R${:.2f}'.format(a1))
else:
    print('O custo da sua viagem será de: R${:.2f}'.format(a2))
print('FIM')



'''distancia = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua viagem será de R${:.2f}'.format(preço))'''


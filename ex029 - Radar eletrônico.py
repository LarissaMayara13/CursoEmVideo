from time import sleep

print('-=-' * 20, 'RADAR ELETRÔNICO', '-=-' * 20)
velocidade = float(input('Qual é a velocidade atual do carro?:'))
print('PROCESSANDO....')
sleep(3)
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80KM/h.')
    print('Você deve pagar a multa de R${:.2f}!'.format((velocidade - 80) * 7))
print('Tenha um bom dia! Dirija com segurança!')



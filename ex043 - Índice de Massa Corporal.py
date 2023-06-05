p = float(input('Qual o seu Peso? (Kg)'))
a = float(input('Qual a sua altura? (m)'))
imc = p / (a * a)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO ')
elif imc <= 25:
    print('Peso Ideal')
elif imc <= 30:
    print('Você está com SOBREPESO')
elif imc <= 40:
    print('OBESIDADE!')
else:
    print('Obesidade Mórbida')
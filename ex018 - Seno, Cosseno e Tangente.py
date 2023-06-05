import trigonometry
num1 = float(input('Digite o valor do angulo:'))
s = trigonometry.sin_ang(num1)
c = trigonometry.cos_ang(num1)
t = trigonometry.tan_ang(num1)
print('Valor do seno do ângulo {} é:{}'.format(num1, s))
print('valor do cosseno do ângulo {} é:{}'.format(num1, c))
print('valor da tangente do ângulo {} é: {}'.format(num1, t))

print('========== BEM-VINDO ==========')
l = float(input('Digite o valor da Largura da parede:'))
a = float(input('Digite o valor da Altura da parede:'))
fa = l * a
ft = fa / 2
print('Sua área é de {}m², e a quantidade de tinta necessária para pinta-la é de {:.2f} litros.'.format(fa, ft))


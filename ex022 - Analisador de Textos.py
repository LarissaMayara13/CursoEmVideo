a1 = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é:{}'.format(a1.upper()))
print('Seu nome em minúsculas é:{}'.format(a1.lower()))
print('Seu nome tem ao todo:{} letras'.format(len(a1)-a1.count(' ')))
a2 = a1.split()
print('Seu primeiro nome é {}, e ele tem {} letras'.format(a2[0], len(a2[0])))























from datetime import date
atual = date.today().year
ano = int(input('Ano de Nascimento:')[:4])
s = atual - ano
a = ano + 18
n = a - atual
print('''Escolha seu gênero:'
[ 1 ] Feminino
[ 2 ] Masculino''')
sexo = int(input('Sua opção:'))
if sexo == 1:
    print('Você não precisa fazer o alistamento militar obrigatório!!')
pass

if sexo == 2:
    print(('Quem nasceu em {} tem {} anos em 2023.'.format(ano, s)))
    if s < 18:
        print('Ainda faltam {} anos para o alistamento.'.format(n))
        print('Seu alistamento será em {}.'.format(a))
    elif s > 18:
        print('Você já deveria ter se alistado há {} anos.'.format(-n))
        print('Seu alistamento foi em {}.'.format(a))
    elif s == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
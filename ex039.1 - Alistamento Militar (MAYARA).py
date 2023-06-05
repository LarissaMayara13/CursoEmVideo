from datetime import date # INCREMENTO DO CÓDIGO DO PROFESSOR
atual = date.today().year
ano = int(input('Ano de Nascimento:')[:4])
s = atual - ano
print('Quem nasceu em {} tem {} anos em 2023.'.format(ano, s))
a = ano + 18
n = a - atual
if s < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(n))
    print('Seu alistamento será em {}.'.format(a))
elif s > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(-n))
    print('Seu alistamento foi em {}.'.format(a))
elif s == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')



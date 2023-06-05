n1 = float(input('Primeira Nota:'))
n2 = float(input('Segunda Nota:'))
m = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if m >= 7:
    print('O aluno está APROVADO!')
elif m >= 5 and m<= 6.9: # 7 > m >=5
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!!')


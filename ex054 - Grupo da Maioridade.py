from datetime import date
cont1 = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu:'.format(c)))
    atual = date.today().year
    ca = atual - ano
    if ca >= 18:
        cont1 = cont1 + 1
    else:
        cont2 = cont2 + 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(cont1))
print('E também tivemos {} pessoas menores de idade.'.format(cont2))


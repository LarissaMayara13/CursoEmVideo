print(' ============== LOJAS GUANABARA ==============')

p = float(input('Preço das Compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/ cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais ou cartão''')

o = int(input('Digite a opção: '))

if o == 1:
    s = p - (p * 10 / 100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(p, s))

elif o == 2:
    s = p - (p * 5 / 100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} à vista no cartão.'.format(p, s))

elif o == 3:
    s = p / 2
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS.'.format(s))

elif o == 4:
    q = int(input('Quantidade de parcelas:'))
    if q < 3:
        print('ERROR! Opção inválida!!')
    else:
        s2 = p + (p * 20 / 100)
        s = s2 / q
        print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(q, s))
        print('Sua compra de R$ {:.2f} vai custar {:.2f} no final.'.format(p, s2))

else:
    print('Opção Inválida de pagamento. Tente novamente!')
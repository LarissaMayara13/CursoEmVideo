n = int(input('Digite um  para ver sua tabuada:'))
for c in range(1, 11):
    s = n * c
    print('{} x {} = {}'.format(n, c, s))
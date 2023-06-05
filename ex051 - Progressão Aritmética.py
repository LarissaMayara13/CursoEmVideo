primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
ultimo = primeiro + (10 - 1) * razao
for c in range(primeiro, ultimo, razao):
    print(c)



'''
primeiro = int(input('Primeiro Termo: ))
razao = int(input('Razão: ))
decimo = primeiro + (10 - 1) * razao
for c in range ( primeiro, decimo + razao, razao)
    print('{}'.format(c), end='-> ')
print('ACABOU')'''

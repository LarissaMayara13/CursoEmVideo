import random
a1 = input('Digite o nome do aluno 1:')
a2 = input('Digite o nome do aluno 2:')
a3 = input('Digite o nome do aluno 3:')
a4 = input('Digite o nome do aluno 4:')
lista = [a1, a2, a3, a4]
s = random.sample(lista, k=len(lista))
# random.shuffle(lista) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< MÉTODO MAIS FÁCIL
# print(' A ordem de apresentação será:')
# print(lista)
print('A ordem de apresentação será:{}'.format(s))

import random
name1 = input('Digite o nome do aluno 1:')
name2 = input('Digite o nome do aluno 2:')
name3 = input('Digite o nome do aluno 3:')
name4 = input('Digite o nome do aluno 4:')
lista = [name1, name2, name3, name4]
s = random.choice(lista)
print('O escolhido para apagar o quadro será:{}'.format(s))

import random
al1 = str(input('aluno 1'))
al2 = str(input('aluno 2'))
al3 = str(input('aluno 3'))
al4 = str(input('aluno 4'))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print(' a lista misturada é :')
print(lista)

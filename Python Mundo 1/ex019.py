import random
al1 = int(input('digite o nome do primeiro aluno '))
al2 = int(input('digite o nome do segundo aluno '))
al3 = int(input('digite o nome do terceiro aluno '))
al4 = int(input('digite o nome do quarto aluno '))
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print(f'o aluno escolhido foi {escolhido} ')
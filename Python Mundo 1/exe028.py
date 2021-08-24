from random import randint
print('---====-----====-----===---=====----====0000000000')
print('Será que você consegue acertar o numero que estou pensando ? ')
print('---====-----====-----===---=====----====0000000000')
print('VAi tentar ? entao digite um numero de 0 a 5 ')
numb = int(input())
comp = randint(0,5)
if comp == numb:
    print('você acertou o numero!!!!!! congratulation')
else:
    print('Voce não acertou dessa vez')
print(f'numero escolhido {numb}, numero pensado {comp}')
from time import sleep
import random



def respostas():
    with open('decisao.txt', 'r') as arquivo:
        lista = [x.strip() for x in arquivo]
        arquivo.close()
    return random.choice(lista)

def pergunta():
    pergunta_usuario = input('Qual a sua pergunta ? ')
    print('Pensando...')
    sleep(3)

def outra_Pergunta():
    other_decision = ''
    while other_decision != 'n' and other_decision != 's':
        other_decision = input('Deseja fazer outra pergunta  (s/n)?')
        other_decision.lower()
    return other_decision

def decisao():
    decision = ''
    while decision != 'n':
        pergunta()
        print()
        print(respostas())
        decision = outra_Pergunta()
    print('Obrigado por perguntar !')

decisao()


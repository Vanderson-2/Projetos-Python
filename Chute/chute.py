from random import randint
class Chute_Valor:
    def __init__(self):  # construtor
        self.valor_inicial = 0
        self.valor_final = 100
        self.random = randint(self.valor_inicial,self.valor_final)


    def digitar_verificar(self):

        try:
            valor = int(input('Chute um número entre 0 e 100'))
            while (valor < 1) or (valor > 100): # verifica se o valor está na faixa
                valor = int(input('Valor digitado deve ser um número entre 0 e 100'))

            return valor  # retorna o valor caso esteja certo

        except ValueError:  # trata o erro se o valor digitado não for um número
            print('Você deve digitar um número')


    def teste(self,valor):
        while valor != self.random: # enquanto o valor digitado for diferente do valor sorteado
            if valor > self.random:
                print('\nVocê errou.Tente novamente.\nTente digitar um valor menor\n')
            else:
                print('\nVocê errou.Tente novamente.\nTente digitar um valor maior\n')
            valor = self.digitar_verificar() # chama a funcao digitar_verificar


    def chutar(self):
        print('Irei pensar em um valor entre 0 e 100 e você terá que adivinhar.')

        valor = self.digitar_verificar()  # chama a função digitar verificar
        valor_sorteio = self.random  # pega o valor do atributo self.random

        self.teste(valor)  # chama a função teste com atributo valor

        print(f'\nParabéns! Você acertou o valor é {valor_sorteio}')




jogar = Chute_Valor()
jogar.chutar()


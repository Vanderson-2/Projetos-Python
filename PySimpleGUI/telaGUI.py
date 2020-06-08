import PySimpleGUI as sg

sg.theme('DarkPurple4')


class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('nome'), sg.Input(size=(18, 0), key='Nome')],
            [sg.Text('idade'),sg.Input(size=(5,0), key='idade')],
            [sg.Text('endereço'), sg.Input(size=(18, 0), key='endereço')],
            [sg.Text('Telefone'), sg.Input(size=(12, 0), key='Telefone')],
            [sg.Text('Sexo : ')],
            [sg.Radio('Feminino', 'sexo', key='Feminino'),
             sg.Radio('Masculino', 'sexo', key='Masculin'),
             sg.Radio('Outros', 'sexo', key='Outros')],
            [sg.Output(size=(30,10))], # O log só exibe os dados do print()
            [sg.Button('Salvar')]
        ]
        # Janela
        self.janela = sg.Window('Dados do usuário', layout)
        # Extrair dados  da janela


    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            dicionario_cadastro = {
            'nome' : self.values['Nome'],
            'endereco'  : self.values['endereço'],
            'telefone' : self.values['Telefone'],
            'idade' : self.values['idade'],
            'masculino' : self.values['Masculin'],
            'Feminino' : self.values['Feminino'],
            'Outros' : self.values['Outros']}

            sexo = ''
            if dicionario_cadastro['masculino']:
                sexo = 'Masculino'
            elif dicionario_cadastro['Feminino']:
                sexo = 'Feminino'
            else:
                sexo = 'Outros'

            print(f"Nome : {dicionario_cadastro['nome']}\nidade {dicionario_cadastro['idade']}\nendereço {dicionario_cadastro['endereco']}\nsexo : {sexo}.")



tela = TelaPython()
tela.Iniciar()
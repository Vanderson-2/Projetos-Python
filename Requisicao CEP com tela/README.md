<h1>Consulta de CEP via API</h1>

<h3>O codigo faz uma requisição ao site do VIACEP através da sua API, com isso ele consegue retornar o CEP em formato JSON.</h3>

	url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
			if url.status_code == 200:
				print('Sucesso')
			elif url.status_code == 400:
				print('Erro 400')

			endereco = url.json()
			
			
			
![TELA DE CEP](https://i.imgur.com/BW7YGrb.png "TELA DE CEP")


	def __init__(self):

        layout = [
                [sg.Text('cep'),sg.Input(size = (25,0), key='CEP')],
                [sg.Button('Buscar')],
                [sg.Output(size=(40,10))]
        ]


        self.tela = sg.Window('Busca de CEP',layout)
		self.button, self.values = self.tela.Read()

![resultado](https://i.imgur.com/bG276t2.png "resultado")

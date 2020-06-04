##Consulta de CEP via API

O codigo faz uma requisição ao site do VIACEP através da sua API, com isso ele consegue retornar o CEP em formato JSON.

	url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
			if url.status_code == 200:
				print('Sucesso')
			elif url.status_code == 400:
				print('Erro 400')

			endereco = url.json()

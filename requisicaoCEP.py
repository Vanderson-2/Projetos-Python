import requests
import json

def consulta_cep(cep):
    url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if url.status_code == 200:
    	print('Sucesso')
    elif url.status_code == 400:
    	print('Erro 400')

    endereco = url.json()

    for k, v in endereco.items():
    	print(k , ' : ' ,v )
    	

if __name__ == '__main__':
	cep = input('Digite um cep')
    consulta_cep('cep')

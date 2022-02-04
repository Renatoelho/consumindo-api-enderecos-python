#!/home/ubuntu/python/api-enderecos-python/.venv/bin/python3

import requests

lista_ceps = ['01153000', '20050000','70714020']
lista_enderecos = []

for cep in lista_ceps:

    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)

    try:
        req = requests.get(url, timeout=3)

        if req.status_code == 200:

            # API acessada com sucesso!

            endereco = req.json()

            lista_enderecos.append([endereco['cep'], 
            			    endereco['logradouro'], 
            			    endereco['complemento'], 
            			    endereco['bairro'], 
            			    endereco['localidade'], 
            			    endereco['uf']])

        else:
            print('Ocorreu o seguinte erro no acesso da API: {}'.format(req.raise_for_status()))

    except Exception as erro: 

        print('Ocorreu o seguinte erro na execução do código: {}'.format(erro))

for item in lista_enderecos:
    print(item)
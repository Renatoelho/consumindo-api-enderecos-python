#!/usr/bin/python3

import requests


lista_ceps: list = ['01153000', '20050000', '70714020']
lista_enderecos: list = []

for cep in lista_ceps:
    url: str = 'https://viacep.com.br/ws/{}/json/'.format(cep)

    try:
        req = requests.get(url, timeout=3)
        if req.status_code == 200:
            # API acessada com sucesso!
            endereco = req.json()
            lista_enderecos.append(
                            [
                                endereco['cep'],
                                endereco['logradouro'],
                                endereco['complemento'],
                                endereco['bairro'],
                                endereco['localidade'],
                                endereco['uf']
                            ]
            )

        else:
            erro = req.raise_for_status()
            print(f'Ocorreu o seguinte erro no acesso da API: {erro}')

    except Exception as erro:
        print(f'Ocorreu o seguinte erro na execução do código: {erro}')

for item in lista_enderecos:
    print(item)

# Consumindo uma API de endereços com Python

### Requisitos mínimos:

>> Sistema operacional Linux (Ubuntu 20.04.2 LTS)  <br/>Memória RAM de 4GB ou mais  <br/>Python 3 instalado

Imagine que você tem uma base de endereços de clientes que esteja incompleta, e que queira atualizar, uma das melhores maneiras seria utilizar uma API e o Python para fazer as requisições. Neste nosso exemplo aqui vamos utilizar a API da [Via CEP](https://viacep.com.br/), onde iremos passar na requisição um determinado CEP e a API vai retornar vários atributos de endereço ligados ao CEP em questão, em seguida esses dados retornados podem ser inseridos em um banco de dados ou em qualquer outra base de dados, em nosso exemplo aqui vamos passar uma lista com alguns números de CEP e iremos obter uma nova lista com vários atributos relacionado a esses CEPs como: bairro, localidade, uf e etc.

Para instalar as bibliotecas necessárias no Python utilize o arquivo *requeriments.txt* e execute o seguinte comando:

```bash
pip install -r requeriments.txt
```

# Código Python para acesso a API

```python
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

            lista_enderecos.append([endereco['cep'], endereco['logradouro'], endereco['complemento'], endereco['bairro'], endereco['localidade'], endereco['uf']])

        else:
            print('Ocorreu o seguinte erro no acesso da API: {}'.format(req.raise_for_status()))

    except Exception as erro: 

        print('Ocorreu o seguinte erro na execução do código: {}'.format(erro))

for item in lista_enderecos:
    print(item)
```

![Acessando API com PYthon](https://drive.google.com/uc?export=view&id=12sfKBnNuzE8c92HZXaZn5gdueh1rgyqE)

>> **Importante:** A utilização da API do [Via CEP](https://viacep.com.br/) aqui é somente com a intenção de contextualizar como seria a execução de requisições para uma determinada API com auxílio da linguagem **Python**, pois no mercado existem várias empresas que fornecem esse tipo de serviço e que seria o mais adequado para solucionar questões desse tipo.


<b>Até breve!</b>

> **Referências:**  <br/><font size="1">Requests, **HTTP for Humans**. Disponível em: <https://docs.python-requests.org/en/latest/>. Acesso em: 1 fev. 2022.  <br/>Via CEP, **Consulte CEPs de todo o Brasil**. Disponível em: <https://viacep.com.br/>. Acesso em: 1 fev. 2022.  <br/></font>

import requests
import os
import json
import sys

from os import path
from requests.auth import HTTPBasicAuth


URLS = {
    'ipca': 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.4447/dados'
}
USERNAME = 'user'
PASSWORD = 'pass'


def ler_arquivo(caminho):
    if not path.isfile(caminho):
        print('O arquivo nao existe!')
        return []

    try:
        with open(caminho, 'r') as fd:
            ret = json.load(fd)
    except Exception as err:
        sys.exit(f'Ocorreu um erro!\nMensagem de erro: {err}')

    return ret


def salvar_arquivo(conteudo, caminho):
    try:
        with open(caminho, 'w') as fd:
            json.dump(conteudo, fd)
    except Exception as err:
        print(f'Ocorreu um erro!\nMensagem de erro: {err}')
        return False

    return True


def coleta_json_de_url(url):
    ret = None
    try:
        """
        req = requests.get(
            url,
            params={'formato': 'json'},
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )
        """
        req = requests.get(url)

        if req.status_code == 200:
            ret = req.json()
        else:
            print('Ocorreu um erro na consulta da url!')
            print('Codigo do erro:', req.status_code)
    except Exception as err:
        print(f'Ocorreu um erro!\nMensagem: {err}')

    return ret


def etl_local():
    datapath = path.join(src_path, 'dados.json')
    dados = formatar_ipca(ler_arquivo(datapath))

    if salvar_arquivo(dados, 'dados_formatados.json'):
        print('Arquivo transformado com sucesso!')


def formatar_ipca(dados):
    for dado in dados:
        dado['valor'] = round(float(dado['valor']) / 100, 4)

    return dados


def main():
    src_path = os.getcwd()
    dados = {}
    for dado, url in URLS.items():
        dados[dado] = coleta_json_de_url(url)

    for nome, conteudo in dados.items():
        if nome == 'ipca':
            conteudo = formatar_ipca(conteudo)

        if salvar_arquivo(conteudo, f'{nome}.json'):
            print(f'Base {nome} salva com sucesso!')


if __name__ == '__main__':
    main()

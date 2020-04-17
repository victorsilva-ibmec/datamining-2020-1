import os
import json
import sys

from os import path


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


def main():
    src_path = os.getcwd()
    datapath = path.join(src_path, 'dados.json')
    dados = ler_arquivo(datapath)
    for dado in dados:
        dado['valor'] = round(float(dado['valor']) / 100, 4)

    if salvar_arquivo(dados, 'dados_formatados.json'):
        print('Arquivo transformado com sucesso!')


if __name__ == '__main__':
    main()

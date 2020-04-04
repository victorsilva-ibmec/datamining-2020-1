"""
Script para ler dados de alunos e armazenar as suas notas.
O script tambem pode calcular as medias das notas armazenadas.

Os alunos são organizados conforme o exemplo:

{
    '111.111.111-11': {
        'nome': <nome>,
        'notas': []
    }
}
"""


def cpf_e_valido(cpf):
    """Valida cpf."""
    return cpf != ''


def adiciona_aluno(alunos):
    ret = alunos

    cpf = input('Informe o cpf do aluno, no formato XXX.XXX.XXX-XX: ')
    if not cpf_e_valido(cpf):
        print('Valor invalido!')
        return ret
    elif cpf in alunos.keys():
        if input('Esse aluno ja foi incluido! Deseja atualizar os dados (s/n)? ') != 's':
            return ret

    nome = input('Informe o nome do aluno: ')
    if cpf not in ret.keys():
        ret[cpf] = {}

    ret[cpf]['nome'] = nome
    return ret


def limpa_alunos():
    return {}


def exibe_alunos(alunos):
    for cpf, dados_aluno in alunos.items():
        print(f'{cpf} - {dados_aluno["nome"]}')

    return alunos


def exclui_aluno():
    nome = input('Informe o nome do aluno a ser excluido: ')
    if nome in alunos:
        alunos.pop(procura_aluno(nome))
    else:
        print('Nao existe ninguem com esse nome!')


def procura_aluno(nome):
    """Busca o indice da lista alunos que tenha o valor nome."""
    for indice, aluno in enumerate(alunos):
        if aluno == nome:
            return indice

    return -1


def salva_lista():
    """Le um nome de arquivo e salva a lista existente dentro da raiz do projeto."""
    arquivo = input('Informe o nome do arquivo para salvar. ')
    if arquivo == '':
        print('Erro! Nome de arquivo invalido.\n')
        return

    with open(arquivo, 'w') as fd:
        fd.write('\n'.join(alunos))

    print(f'Sucesso ao salvar o arquivo {arquivo}!\n')


def abre_lista():
    """Le um nome de arquivo e abre a lista que esta na raiz do projeto, se existir."""
    arquivo = input('Informe o nome do arquivo para abrir.')
    with open(arquivo, 'r') as fd:
        lista = fd.read().split('\n')

    if not alunos:
        alunos.extend(lista)
    else:
        if input('Ja existe uma lista aberta! Deseja sobrescrever (s/n)? ') == 's':
            limpa_lista()
            alunos.extend(lista)
        else:
            print('Acrescentando novos alunos na lista ja aberta...')
            for nome in lista:
                if nome not in alunos:
                    alunos.append(nome)


def adiciona_notas(alunos):
    """Adiciona uma nota para cada aluno cadastrado."""
    ret = alunos
    for cpf, dados_aluno in ret.items():
        if 'notas' not in dados_aluno.keys():
            dados_aluno['notas'] = []

        try:
            nota = float(input(f'Informe a nota do aluno {cpf} - {dados_aluno["nome"]}: '))
        except ValueError:
            print('Nota invalida! Considerando nota zero...')
            nota = 0.0

        dados_aluno['notas'].append(nota)

    return ret


def exibe_notas(alunos):
    for cpf, dados_aluno in alunos.items():
        if 'notas' in dados_aluno.keys():
            print(f'{cpf} - {dados_aluno["nome"]} - {dados_aluno["notas"]}')

    return alunos


OPCOES = {
    '': exit,
    'a': adiciona_aluno,
    'e': exibe_alunos,
    'x': exclui_aluno,
    'l': limpa_alunos,
    's': salva_lista,
    'o': abre_lista,
    'n': adiciona_notas,
    'b': exibe_notas
}


def main():
    alunos = {
        '111': {
            'nome': 'ola'
        },
        '222': {
            'nome': 'mundo'
        }
    }

    while True:
        opcao = input('Entre com uma das opcoes a seguir (ou aperte ENTER para sair):\n'
                      'a - Adicionar novo aluno\n'
                      'e - Exibe todos os alunos cadastrados\n'
                      'x - Excluir um aluno\n'
                      'l - Limpar lista aberta\n'
                      's - Salvar a lista em um arquivo\n'
                      'o - Abrir uma lista salva\n'
                      'n - Adiciona uma nota para cada aluno\n'
                      'b - Exibe as notas de cada aluno\n')
        if opcao in OPCOES.keys():
            alunos = OPCOES[opcao]() if opcao == 'l' else OPCOES[opcao](alunos)
            print(alunos)
        else:
            print(f'Opcao {opcao} invalida!')


if __name__ == '__main__':
    main()

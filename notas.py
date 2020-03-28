"""
Script para ler dados de alunos e armazenar as suas notas.
O script tambem pode calcular as medias das notas armazenadas.
"""


alunos = ['Ola', 'Mundo']


def adiciona_aluno():
    nome = input('Informe o nome do aluno: ')
    if nome in alunos:
        print('Esse aluno ja foi incluido!')
    else:
        alunos.append(nome)


def exibe_alunos():
    for aluno in alunos:
        print(aluno)


def exclui_aluno():
    nome = input('Informe o nome do aluno a ser excluido: ')
    if nome in alunos:
        for indice, aluno in enumerate(alunos):
            if aluno == nome:
                alunos.pop(indice)
                break
    else:
        print('Nao existe ninguem com esse nome!')


def procura_aluno(nome):
    """Busca o indice da lista alunos que tenha o valor nome."""
    pass


def main():
    while True:
        opcao = input('Entre com uma das opcoes a seguir (ou aperte ENTER para sair):\n'
                      'a - Adicionar novo aluno\n'
                      'e - Exibe todos os alunos cadastrados\n'
                      'x - Excluir um aluno\n')
        if opcao == '':
            print('Saindo...')
            break
        elif opcao == 'a':
            adiciona_aluno()
        elif opcao == 'e':
            exibe_alunos()
        elif opcao == 'x':
            exclui_aluno()
        else:
            print(f'Opcao {opcao} invalida!')


if __name__ == '__main__':
    main()

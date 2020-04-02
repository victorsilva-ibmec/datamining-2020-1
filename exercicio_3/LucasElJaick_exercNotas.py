
alunos = []


def adiciona_aluno():
    nome = input('Informe o nome do aluno: ')
    nomeFormatado = nome.strip().upper()
    if nomeFormatado in alunos:
        print('Esse aluno ja foi incluido!')
    else:
        alunos.append(nomeFormatado)


def exibe_alunos():
    for aluno in alunos:
        print(aluno)


def exclui_aluno():
    nome = input('Informe o nome do aluno a ser excluido: ')
    nomeFormatado = nome.strip().upper()
    if nomeFormatado in alunos:
        for indice, aluno in enumerate(alunos):
            if aluno == nomeFormatado:
                alunos.pop(indice)
                print("Aluno excluido com sucesso")
                break
    else:
        print('Nao existe ninguem com esse nome!')


def procura_aluno():
    nome = input('Informe o nome do aluno a ser procurado: ')
    nomeFormatado = nome.strip().upper()
    quantidade = len(alunos)
    temAluno = 0

    for i in range(quantidade):
        if nomeFormatado == alunos[i]:
            print("o indice e " + str(i), " ")
            temAluno = 1

    if temAluno == 0:
        print("O aluno nao esta na lista")


def main():
    while True:
        opcao = input('Entre com uma das opcoes a seguir (ou aperte ENTER para sair):\n'
                      'a - Adicionar novo aluno\n'
                      'e - Exibe todos os alunos cadastrados\n'
                      'x - Excluir um aluno\n'
                      'p - Procurar um aluno\n')
        if opcao == '':
            print('Saindo...')
            break
        elif opcao == 'a':
            adiciona_aluno()
        elif opcao == 'e':
            exibe_alunos()
        elif opcao == 'x':
            exclui_aluno()
        elif opcao == 'p':
            procura_aluno()
        else:
            print(f'Opcao {opcao} invalida!')


if __name__ == '__main__':
    main()

def exercicio_10():

    lst1 = []
    lst2 = []
    lst3 = []

    "inclusão lista 1"
    print("PRIMEIRO VETOR DE ELEMENTOS")
    for i in range (10):
        lst1.append(input("insira o elemento"))

    "inclusão lista 2"
    print("SEGUNDO VETOR DE ELEMENTOS")
    for n in range (10):
        lst2.append(input("insira o elemento"))



    "inclusão na terceira lista"
    for j in range (10):
        lst3.append(lst1[j])
        lst3.append(lst2[j])



def exercicio_12():
    lstTemp = []
    for i in range(12):
        print("Diga a temperatura do mês", i + 1)
        lstTemp.append(float(input("insira  aqui")))

    ma = sum(lstTemp) / 12
    print(lstTemp)
    print(ma)




def exercicio_14():
    lst = []
    q = 0
    num=0
    while num !=-1:
        num = float(input('Entre com o valor da nota ou -1 para encerrar'))
        if num >= 0.0:
            lst.append(num)

    media = float((sum(lst))/len(lst))
    "Printa a quantidade de notas, quais sao as notas, a soma das notas e a media"
    qtd = len(lst)
    print(qtd)
    print(lst)
    print(sum(lst))
    print(media)

    "numeros acima da media"
    for i in range(len(lst)):
      if lst[i] > media:
        print(lst[i])
        q=q+1
    print(q)
    "qtd acima da media"

    "do ultimo para o primeiro"
    for i in range(len(lst)):
      print(lst[qtd - i])



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
    if nome in alunos:
        for indice, aluno in enumerate(alunos):
            if aluno == nome:
                return indice
    else:
        print("Não há esse nome")


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

"""
Script para ler dados das notas dos alunos e armazená-las.
O script também pode calcular as médias das notas armazenadas.
"""
alunos = []

def adicionar_aluno():
    nome = input('Informe o nome do aluno: ')
    if nome in alunos:
        print('Este aluno já está na lista!')
    else:
        alunos.append(nome)

def exibir_alunos():
    for indice, aluno in enumerate(alunos):
        print(indice, '-', aluno)

def excluir_aluno():
    nome = input('Informe o nome do aluno a ser excluído: ')
    if nome in alunos:
        for indice, aluno in enumerate(alunos):
            if aluno == nome:
                alunos.pop(indice)
                break
    else:
        print('Não existe aluno com este nome!')

def procura_aluno():

    """Busca o índice da lista alunos que tenha o valor do nome escolhido"""

    nome = input('Informe o nome do aluno que deseja procurar: ')
    if nome in alunos:
        for indice, aluno in enumerate(alunos):
            if aluno == nome:
                print(f'O indice do(a) aluno(a) {nome} é {indice}')
            else:
                pass
    else:
        print(f'O nome {nome} não consta na lista de alunos!')

def main():
    while True:
        option = input('\na - Adicionar novo aluno;\n'
                       'b - Exibe todos os alunos cadastrados;\n'
                       'c - Excluir aluno;\n'
                       'd - Procurar aluno;\n'
                       'Entre com uma das opções acima (Ou aperte ENTER para sair): ')
        if option == '':
            print('\nSaindo...')
            break
        elif option == 'a':
            print('\nAdicionar aluno')
            adicionar_aluno()
        elif option == 'b':
            print('\nLista de alunos:')
            exibir_alunos()
        elif option == 'c':
            print('\nExcluir aluno')
            excluir_aluno()
        elif option == 'd':
            print('\nProcurar aluno')
            procura_aluno()
        else:
            print(f'\nOpção {option} inválida!')

if __name__ == '__main__':
    main()



#Exercício 10:
def uniao_vetorial():
    vetor_final = []
    vetor_1 = input('Insira dez valores separados por vírgula para o vetor 1: ').split(',')
    vetor_2 = input('Insira dez valores separados por vírgula para o vetor 1: ').split(',')
    contador_1 = 0
    contador_2 = 0
    for i in range(20):
        if i % 2 == 0:
            vetor_final.append(vetor_1[contador_1])
            contador_1 += 1
        else:
            vetor_final.append(vetor_2[contador_2])
            contador_2 += 1
    print(vetor_final)
#uniao_vetorial()



#Exercício 12:
def analise_de_temperatura():
    lista_de_temperaturas = []
    lista_de_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                      'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    contador_1 = 0
    contador_2 = 0
    for temperatura in range(12):
        valor = int(input(f'Insira a temperatura de {lista_de_meses[contador_1]}: '))
        lista_de_temperaturas.append(valor)
        contador_1 += 1

    media_anual = round(sum(lista_de_temperaturas)/12, 2)

    for temperatura in lista_de_temperaturas:
        if temperatura > media_anual:
            print(f'A temperatura do mês de {lista_de_meses[contador_2]}, no valor de {lista_de_temperaturas[contador_2]},'
                  f' ficou acima da média anual de {media_anual}!')
        else:
            pass
        contador_2 += 1
#analise_de_temperatura()



#Exercício 14:
def programa_de_notas():
    lista_de_notas = []
    while True:
        nota = int(input('Insira uma nota: '))
        if nota != -1:
            lista_de_notas.append(nota)
        else:
            break

    contador = len(lista_de_notas) - 1

    print(f'Foram inseridas um total de {len(lista_de_notas)} notas!')
    print('Notas inseridas:', lista_de_notas)
    print('Notas inseridas na ordem inversa:')
    for number in range(len(lista_de_notas)):
        print(lista_de_notas[contador])
        contador -= 1

    media_das_notas = sum(lista_de_notas)/len(lista_de_notas)
    print('Soma das notas: ', sum(lista_de_notas))
    print('Média das notas: ', media_das_notas)

    quantidade_de_notas_acima_da_media = 0
    for nota in lista_de_notas:
        if nota > media_das_notas:
            quantidade_de_notas_acima_da_media += 1

    print('Quantidade de notas acima da média: ', quantidade_de_notas_acima_da_media)
    print('Programa encerrado!')
#programa_de_notas()


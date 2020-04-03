def procura_aluno():
    """Busca o indice da lista alunos que tenha o valor nome."""

    nome = input("Qual o nome do aluno que voce procura? ")
    if nome in alunos:
        print(f'O aluno procurado esta localizado {alunos.index(nome)}.')
    else:
        print(f'O nome {nome} não consta nesta lista!')
        pass


def exerc_10():
    lista1 = []
    lista2 = []
    lista3 = []

    for i in range(10):
        valor1 = input('Insira um valor para primeira lista:')
        lista1.append(valor1)
        valor2 = input('Insira um valor para seguinda lista:')
        lista2.append(valor2)
        lista3.append(lista1[i])
        lista3.append(lista2[i])

    # print(lista1)
    # print(lista2)
    print(lista3)
    # coloquei para printar as lista 1 e 2 apenas para certificar que estava realizando corretamente.


def exerc_12():
    temperatura = []
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
    media = 0
    acimaMedia = {}

    for i in range(len(meses)):
        temperatura.append(float(input('Informe a Temperatura media de ' + meses[i] + ':\n')))

        media = sum(temperatura) / len(meses)

    for i in range(len(meses)):
        if temperatura[i] > media:
            acimaMedia.update({meses[i]: temperatura[i]})

    print('Media das temperaturas anual: ' + str(media))
    print('Meses com temperaturas acima da media anual: ' + str(acimaMedia))


def exerc_14():
    lista = []
    acima_media = []

    while True:
        num = float(input('Insira um numero, caso queira encerra a importação de dados, digiti -1:'))
        if num == -1:
            break
        else:
            lista.append(num)
    # quantidade de numeros e a lista completa
    print(f'Quatidade de valores que foram lidos: {len(lista)}')
    print(f'A lista e formada por esses valores na ordem que forom informados: {lista}')

    # lista de forma inversa
    lista.reverse()
    print('A lista e formada por esses valores na ordem inversa que forom informados: ')
    for i in lista:
        print(i)

    # soma dos valores
    print(f'A soma dos valores são: {sum(lista)}')

    # media dos valores
    media = sum(lista) / len(lista)
    print(f'A media dos valores são: {media} ')

    # quantidade de valores acima da media calculada
    for i in range(len(lista)):
        if lista[i] > media:
            acima_media.append(num)
    print(f'Quatidade de numeros acima da media são: {len(acima_media)}')

    # Encerrando com uma mensagem
    print('O programa finalizado !!!!')


def main():
    exerc_14()


if __name__ == '__main__':
    main()

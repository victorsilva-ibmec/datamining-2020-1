# incluindo o procura alunos na questão resolvida no notas.py
alunos = ['maria', 'joao', 'antonia']
def procura_aluno():
    nome = input('Qual o nome do aluno que vc deseja procurar?')
    if nome in alunos:
        print('Esse aluno está na lista')
        for i, v in enumerate(alunos):
            if v == nome:
                print(f'O aluno {nome} pertence ao indice {i}!')
    else:
        print(f'Este nome {nome} não se encontra na lista de alunos!')

#questão 10
def intercala():
    lista1 = []
    lista2 = []
    for c in range(4):
        valores1 = int(input(f'Digite o indice {c}'))
        lista1.append(valores1)
    print(lista1)
    for v in range(4):
        valores2 = int(input(f'Digite o indice {v}'))
        lista2.append(valores2)
    print(lista2)

    i = 0
    j = 0
    k = 0
    intercalada = []
    while i < len(lista1)+len(lista2):
        if j < len(lista1):
            intercalada.append(lista1[j])
            i = i + 1
            j = j + 1
        if k < len(lista2):
            intercalada.append(lista2[k])
            i = i + 1
            k = k + 1
    print(f' A lista intercalada é {intercalada}')

# questão 12 (professor tive dificuldade em resolver incluindo a lista que eu criei meses, para relacionar com a teperatura daquele mes
def temp_med():
    lst = []
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    temp_maior_med = []
    for c in range(1,13):
        temperatura = float(input(f'Qual a temperatura media do mes {c}?'))
        lst.append(temperatura)
    media = sum(lst) / len(lst)
    print(f' A media é {media}!')
    for celsius in lst:
        if celsius > media:
            temp_maior_med.append(celsius)
    print(f' As temperaturas maiores que a media são: {temp_maior_med}')


# questão 14
def ler_num():
    lst = []
    maior_med = []
    while True:
        numeros = int(input(' Insira um numero, caso queira encerrar aperte -1...'))
        if numeros == -1:
            break
        else:
            lst.append(numeros)
    print(f' A lista é formada por: {lst}')
    print(f' A quantidade de valores lidos é {len(lst)}')
    media = sum(lst) / len(lst)
    print(f' a média é {media}')
    print(f'A soma dos numeros é {sum(lst)}')
    for numero in lst:
        if numero > media:
            maior_med.append(numero)
    print(f' Os numeros maiores que a média são {maior_med}')
    print(f' Sendo a quantidade de numeros maiores que a media: {len(maior_med)}')

    lst.reverse()
    print('Os valores inversamente são:')
    for v in lst:
        print(v)

    print('----------O programa encerrou aqui------------')


def main():
    procura_aluno()
    intercala()
    temp_med()
    ler_num()





if __name__=='__main__':
    main()
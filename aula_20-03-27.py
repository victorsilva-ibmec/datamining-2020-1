def ler_5num():
    lst = []
    for cont in range(5):
        valor = int(input('Insira um valor.'))
        lst.append(valor)

    print(lst)


def ler_10num():
    lst = []
    for cont in range(10):
        valor = float(input('Insira um valor.'))
        lst.append(valor)

    for cont in range(10):
        print(lst[9 - cont])


def media_4notas():
    lst = []
    for cont in range(4):
        nota = float(input('Informe uma nota.'))
        lst.append(nota)

    print('Notas lidas:')
    for nota in lst:
        print(nota)

    med = sum(lst) / 4
    print('Media:', med)


def media(lst):
    for nota in lst:
        print(nota)

    med = sum(lst) / len(lst)
    print('Media:', med)


def par_ou_impar():
    lst = []
    par = []
    impar = []
    for cont in range(4):
        valor = int(input('Informe um inteiro.'))
        lst.append(valor)
        if valor % 2 == 0:
            par.append(valor)
        else:
            impar.append(valor)

    print('Lista completa:')
    print(lst)
    print('Valores pares:')
    print(par)
    print('Valores impares:')
    print(impar)


def media_alunos():
    alunos = []
    for aluno in range(10):
        notas = []
        for cont2 in range(4):
            nota = float(input(f'Informe a nota do aluno {aluno}.'))
            notas.append(nota)

        med = sum(notas) / 4
        alunos.append(med)

    print('Medias:')
    print(alunos)
    al_aprovados = 0
    for aluno in alunos:
        if aluno >= 7:
            al_aprovados += 1

    print('Numero de alunos aprovados:', al_aprovados)


def soma():
    lst = []
    while True:
        dado = input('Insira um numero ou aperte ENTER para cancelar: ')
        if dado == '':
            break
        else:
            lst.append(float(dado))

    print(f'Lista de valores inseridos:\n{lst}')
    print(f'A soma dos valores e {sum(lst)}.')
    return sum(lst)


def multiplicacao():
    lst = []
    while True:
        dado = input('Insira um numero ou aperte ENTER para cancelar: ')
        if dado == '':
            break
        else:
            lst.append(float(dado))

    print(f'Lista de valores inseridos:\n{lst}')
    prod = 1
    for num in lst:
        prod = prod * num
    print(f'O produto dos valores e {prod}.')
    return prod


def subtracao(num1):
    num2 = float(input('Informe o numero a ser subtraído: '))

    print(f'{num1} - {num2} = {num1 - num2}')
    return num1 - num2


def divisao(dividendo):
    divisor = float(input('Informe o divisor: '))

    print(f'{dividendo} / {divisor} = {dividendo / divisor}')
    return dividendo / divisor


def calculadora():
    valor = 0
    while True:
        print(f'Valor atual: {valor}')
        operador = input('Informe a operacao desejada (+, -, *, /) ou aperte ENTER para sair: ')
        if operador == '':
            print('Saindo da calculadora...')
            break
        elif operador in ['+', '-', '*', '/']:
            if operador == '+':
                valor += soma()
            elif operador == '-':
                valor = subtracao(valor)
            elif operador == '/':
                valor = divisao(valor)
            else:
                valor = valor * multiplicacao()
        else:
            print(f'Erro! Operador {operador} nao definido!')


def main():
    calculadora()


if __name__ == '__main__':
    main()

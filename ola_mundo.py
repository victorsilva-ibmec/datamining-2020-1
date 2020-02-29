# Precedencia de operacoes:
# ** (potencia)
# * / (multiplicacao e divisao)
# + - (soma e subtracao)


def faz_conta():
    return 0


def oi():
    print('oi')
    print('oi')


def soma_dois_valores(valor1, valor2):
    return valor1 + valor2


def raiz(valor, base):
    return valor ** (1 / base)


def e_par(valor):
    return (valor % 2) == 0


def div_por_seis(valor):
    return ((valor % 2) == 0) and ((valor % 3) == 0)


def testes():
    print(div_por_seis(7))
    print(div_por_seis(9))
    print(div_por_seis(12))
    x = soma_dois_valores(3, 4)
    print(x)
    x = soma_dois_valores(2, 8)
    print(x)
    x = raiz(9, 2)
    print(x)
    print(e_par(4))
    print(e_par(5))


def testa_par():
    """Le um valor inserido pelo usuario, verifica se o valor e par e retorna uma mensagem."""
    parada = False
    while parada == False:
        valor = input('Insira um valor numérico, ou aperte ENTER para encerrar...\n')
        if valor == '':
            parada = True
        elif e_par(int(valor)) == True:
            print('O valor inserido é par.')
        else:
            print('O valor inserido é ímpar.')


def dez_mult_tres():
    """Imprime os primeiros 10 numeros nao negativos multiplos de 3."""
    cont = 0
    numero = 1
    while cont < 10:
        if numero % 3 == 0:
            print(numero)
            cont += 1
        numero += 1  # numero = numero + 1


dez_mult_tres()

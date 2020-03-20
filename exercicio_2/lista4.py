def exercicio_3(peso, exc, multa):
    peso = int(input('Quantos quilos de peixe você pescou hoje? '))
    if peso > 50:
        exc = peso - 50
        multa = exc * 4
        print('Multa a pagar de R$', multa, '.')
    else:
        print('Não há multa.')




def exercicio_5(area_pintura, latas, preco):
    import math
    area_pintura = int(input('Insira o tamanho em metros quadrados da área a ser pintatda:'))
    latas = math.ceil(area_pintura / (3*18))

    preco = latas * 80

    print('O número de latas necessário para pintar será ', latas, ' e o preco a pagar será de R$',preco)


def exercicio_12(a, b, c):
    a = int(input('Insira a.'))
    b = int(input('Insira b.'))
    c = int(input('Insira c.'))

    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("A raiz é negativa.")

    else:
        raiz_delta = delta ** (1/2)
        x1 = (-b + delta) / (2 * a)
        x2 = (-b - delta) / (2 * a)
        print('As raizes são: \nx1 =', x1, ' e x2 = ', x2, '.')




def exercicio_18(termo_n, n1, n2):
    termo_n = int(input('Quantos termos?'))
    n1 = 0
    n2 = 1
    cont = 0

    print(n2)

    while cont < termo_n:

        nf = n1 + n2
        print(nf)

        n2 = nf
        n1 = n2
        cont = cont + 1


def exercicio_21(total):

    votoa = 0
    votob = 0
    votoc = 0

    total = int(input('Insira o número total de eleitores.'))

    for i in range(total):
        voto = input('Qual o seu candidato? A, B ou C?')

        if voto == 'A':
            votoa = votoa + 1
        elif voto == 'B':
            votob = votob + 1
        else :
            votoc = votoc + 1


    print('Quantidade de votos:\n A:', votoa, '\nB:', votob, '\nC:',votoc)



def main():
    
    exercicio_3(-10, 2, 85)

    exercicio_5(54, 5, 9)

    exercicio_12(1, 6, 65)

    exercicio_18(8, 2, 2)

    exercicio_21(20)


if __name__ == '__main__':
    main()

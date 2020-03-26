
def exercicio_3(peso, excesso, multa):

    n = int(input('Insira o numero de peixes'))
    pesopeixe = float(input('Insira o peso unitario dos peixes'))

            peso = float(n * pesopeixe)
            excesso = float(peso - 50)
            multa = float(excesso * 4)

    print('Peso total: '+ peso)
    print('Excesso total: '+ excesso)
    print('Multa a pagar: '+ multa)




def exercicio_5(latas, custo):

    metros2 = float(input('Insira os metros quadrados a serem mintados:'))

    latas = int(metros2 / 6) + 1
    custo = latas * 80

    print('Numero de latas necessarios é: '+ latas)
    print('Custo total é: ' + custo)


def exercicio_12(a, b, c):
    return print(bhaskara1)
    return print(bhaskara2)

a = print('Insira o valor de a')
b = print('Insira o valor de b')
c = print('Insira o valor de c')

delta = (b ** 2) - (4 * a * c)
if delta < 0:
        print("A raiz é negativa.")

    else:
        raiz_delta = delta ** (1/2)
        bhaskara1 = (-b + delta) / (2 * a)
        bhaskara2 = (-b - delta) / (2 * a)




def exercicio_18(termo_n):

    n = int(input('Insira o tamanho da série'))
    n1 = 1
    n2 = 1

        for i in range(n-2)



 print('')





def exercicio_21(total_eleitores):

    total_eleitores = int(input('Insira o total de Eleitores!'))

votos1=0
votos2=0
votos3=0

    for i in range(total_eleitores)
        voto = int(input('1, 2 ou 3?'))

        if voto = 1
            votos1 = votos1 + 1
        else
            if voto= 2
                votos2= votos2 + 1
            else
                votos3 = votos3 + 1

    print('Os votos em 1 foram:'+votos1)
    print('Os votos em 2 foram:'+votos2)
    print('Os votos em 3 foram:'+votos3)




def main():
    exercicio_3(-10)
    exercicio_3(4.25)
    exercicio_3(62.8)
    exercicio_5(54)
    exercicio_5(63.9)
    exercicio_5(25)
    exercicio_12(1, 0, 0)
    exercicio_12(5, 2, 0)
    exercicio_12(2, 4, 6)
    exercicio_18(4)
    exercicio_18(8)
    exercicio_21(5)
    exercicio_21(20)


if __name__ == '__main__':
    main()

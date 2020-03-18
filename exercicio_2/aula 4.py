"""Template para os exercicios 3, 5, 12, 18 e 21 da Aula 04."""

def exercicio_3(peso):
    if peso  > 50:
        excesso = peso - 50
        multa = excesso * 4
    else:
        multa = 0
    print('João deverá pagar uma multa de R$', multa,'.\n\n')

def exercicio_5(area_pintura):
    l = area_pintura / 3
    if area_pintura % 54 == 0:
        latas = area_pintura / 54
    else: latas = int((area_pintura / 54) + 1)
    print('É preciso de', latas, 'latas de tinta. Isso custará R$', latas * 80, '.\n\n')


def exercicio_12(a, b, c):
    x = (b ** 2) - (4 * a * c)
    x1 = 0
    x2 = 0
    if x >= 0:
        x = x ** (1 / 2)
        x1 = (-b + x) / (2 * a)
        x2 = (-b - x) / (2 * a)
        print("As raízes da equação são: ", x1, " e", x2, '.\n\n')
    else:
        print("Não é possível resolver: raízes negativas.\n\n")


def exercicio_18(termo_n):
    ult = 1
    penult = 1
    if (termo_n == 1) or (termo_n == 2):
        print('1\n\n')
    else:
        for i in range(2, termo_n):
            termo_n = ult + penult
            penult = ult
            ult = termo_n
            i += 1
        print(termo_n, '\n\n')


def exercicio_21(total_eleitores):
    votos1 = 0
    votos2 = 0
    votos3 = 0
    votos_tot = 0
    while (votos_tot < total_eleitores):
        v = int(input("Digite o número do candidato desejado.\n"))
        if (v == 1):
            votos1 = votos1 + 1
        elif (v == 2):
            votos2 = votos2 + 1
        elif (v == 3):
            votos3 = votos3 + 1
        votos_tot = votos_tot + 1
    print("Candidato 1:", votos1, "votos.")
    print("Cadidato 2:", votos2, "votos.")
    print("Candidato 3:", votos3, "votos.\n\n")


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
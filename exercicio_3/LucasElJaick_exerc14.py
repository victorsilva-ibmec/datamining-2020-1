def exer14 ():
    lst = []
    while True:
        dado = float(input('Insira a nota : '))
        if dado == -1:
            break
        else:
            lst.append(float(dado))

    quantidade = len(lst)
    print("O total de valores lidos e: ", quantidade)

    print("\n Valores lidos em ordem: ", lst)

    print("\n Valores na Ordem reversa: ")
    lst.reverse()
    for i in range(quantidade):
        print("\n", lst[i])

    soma = float(sum(lst))

    print("\n A Soma e: " , soma )

    media = float(soma/quantidade)

    print("\n A media e: " , media )

    print("\n Os valores acima da media sao: ")
    acimaMedia = 0
    for i in range(quantidade):
        if lst[i]> media:
            print(lst[i], " ")
            acimaMedia = acimaMedia + 1

    print("\n O total de valores acima da media e: ", acimaMedia)

    if media < 7:
        print("\n Sua media e: ", media, " Nao Passou!")
    else:
        print("\n Sua media e: ", media, " Passou!")

def main ():
    exer14()

main()
"""Template para os exercicios 8, 11, 12 e 14 da Aula 02."""
def exercicio_8(valor):
    parte_inteira = 0
    while parte_inteira + 1 <= valor:
        parte_inteira += 1
    parte_fracionaria = valor - parte_inteira
    print('A parte inteira e:', parte_inteira , 'e a parte fracionaria e:', parte_fracionaria)

def exercicio_11():
    num_bois = int(input('Digite a quantidade de bois.\n'))
    peso_max = 0
    iden_max = 0
    for i in range(num_bois):
        iden = int(input('Digite o numero da identificação do boi:\n'))
        peso_boi=int(input('Digite o peso do boi:\n'))
        if peso_boi > peso_max:
            peso_max = peso_boi
            iden_max = iden
    print('O boi mais pesado é o boi com identificação:', iden_max,'com peso de :', peso_max)


def exercicio_12():
    soma = 0
    qtde= int(input('Digite a quantidade de numeros:'))
    for i in range(qtde):
        num=int(input('Digite um numero:'))
        soma = soma + num
    media = soma / qtde
    print('A media dos numeros e:', media)


def exercicio_14(valor_fah):
    celsius = 5*(valor_fah-32) / 9
    print('A temperatura em graus celsius e:',celsius)


def main():
    exercicio_8(4.85)
    exercicio_8(5.5)
    exercicio_8(16)
    exercicio_11()
    exercicio_12()
    exercicio_14(232)
    exercicio_14(18.33)
    exercicio_14(-150)


if __name__ == '__main__':
    main()
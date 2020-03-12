
def exercicio_8(valor):
    inteira = int(valor)
    frac = valor - inteira
    print('Parte inteira: ', str(inteira), '\nParte fracionária: ',  str(frac), "\n")


def exercicio_11():
    lstid = []
    lstpeso = []
    for i in range(3):
        identidade,peso = input("ID e peso (separados por vírgula): \n").split(',')
        lstid.append(identidade)
        lstpeso.append(float(peso))
    mais_pesado = list(max(zip(lstpeso,lstid)))
    print("\nO boi mais pesado é o de ID: ", str(mais_pesado[1]), "e peso: ", str(mais_pesado[0]), "\n")

def exercicio_12():
    soma = 0
    for i in range(10):
        num = int(input("Digite um numero: "))
        soma = soma + num
    media = soma / 10
    print('Média aritmética: ', str(media))


def exercicio_14(fah):
    celsius = (5*(fah - 32))/9
    print('\nA temperatura em Celsius é: ', str(celsius))


def main():
    exercicio_8(4.85)
    exercicio_8(5.5)
    exercicio_8(16)
    exercicio_11()
    exercicio_12()
    exercicio_14(232)

main()

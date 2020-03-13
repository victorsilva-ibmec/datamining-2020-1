
def exercicio_8(valor):
    inteiro = int(valor)
    fracionária = valor - inteiro
    print('Parte inteira igual a: ', str(inteiro), '\nParte fracionária igual a: ',  str(fracionária), "\n")


def exercicio_11():
    nid = []
    npeso = []
    for i in range(3):
        numero_identidade,peso = input(" Numero de identificacao e peso (separados por vírgula): \n").split(',')
        nid.append(numero_identidade)
        npeso.append(float(peso))
    mais_pesado = list(max(zip(nid,npeso)))
    print("\nO boi mais pesado é o de numero de identificacao: ", str(mais_pesado[1]), "e peso: ", str(mais_pesado[0]), "\n")

def exercicio_12():
    soma_numeros = 0
    for i in range(10):
        num = int(input("Digite um numero: "))
        soma_numeros = soma_numeros + num
    media = soma_numeros / 10
    print('Média aritmética: ', str(media))


def exercicio_14(fah):
    fah = float(input(" digite a temperatura em fahrenheit: "))
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

                      
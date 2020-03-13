def exercicio_8(valor):
    inteiro = int(valor)
    fracionario = valor - inteiro
    print('A parte inteira é', str(inteiro), 'e a parte fracionária é ',  str(fracionario))


def exercicio_11():
    gado_id = []
    gado_peso = []
    for i in range(3):
        numero,quilo = input("Número e quilo\nExemplo: 01,50\nInsira igual ao exemplo:").split(',')
        gado_id.append(numero)
        gado_peso.append(float(quilo))
    mais_pesado = list(max(zip(gado_id,gado_peso)))
    print("O gado mais pesado é o de número", str(mais_pesado[0]), "e pesa", str(mais_pesado[1]), "quilos")

def exercicio_12():
    total = 0
    for i in range(10):
        number = int(input("Digite um numero: "))
        total = total + number
    media = total / 10
    print("A média dos 10 números anteriores é", str(media))


def exercicio_14(fahren):
    celsius = (5*(fahren - 32))/9
    print('A tempura em Celsius é de', str(celsius), 'graus')


def main():
    exercicio_8(4.85)
    exercicio_8(5.5)
    exercicio_8(16)
    exercicio_11()
    exercicio_12()
    exercicio_14(232)

main()
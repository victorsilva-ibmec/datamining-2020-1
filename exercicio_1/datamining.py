
def exercicio_8(valor, divisor):
    valor = int(input('Insira um número para dividi-lo.\n'))
    divisor = int(input('Insira um divisor.\n'))

    print(valor / divisor)

def exercicio_11(max_peso, max_id):
    max_id = ''
    max_peso = 0
    for i in range(3):
        identidade = input('Insira a identidade do animal.\n')
        peso = float(input('Insira o peso.\n'))
        if peso > max_peso:
                max_peso = peso
                max_id = identidade

    print('A identidade do animal é', max_id, 'e o peso dele é', max_peso, '.')


def exercicio_12(num, total_sum,numbers):
    num = int(input('Quantos números? '))
    total_sum = 0
    for n in range(num):
        numbers = float(input('Insira o número: '))
        total_sum += numbers
    avg = total_sum / num
    print('A média de', num, 'números é :', avg)


def exercicio_14(valor):
    valor = int(input('Insira temperatura em Fahrenheits: '))
    c = (5 * (valor - 32 ) / 9)

    print('A temperatura em Celcius é:', c)


'''pq ele calcula qualquer numero indifernte do q eu coloque dentro dos parenteses dos exercicios na def main  ? '''
def main():
    exercicio_8(5,2)

    exercicio_11(5, 6)
    exercicio_12(5,5,3)

    exercicio_14(5)


if __name__ == '__main__':
    main()

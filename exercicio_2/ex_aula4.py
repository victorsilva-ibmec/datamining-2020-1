#aula 4
#exerc 3
def peso_peixe():
    excesso = 0
    peso = float(input('Qual o peso do peixe ?\n'))
    if peso > 50:
        excesso = peso - 50
        print('Você excedeu o peso do peixe.')
        print(f'Você excedeu em {excesso} kilos')
        print(f'Deve pagar de multa por kilo em excesso {excesso*4} reais')
    else:
        print('Você está dentro do limite')

# exerc 5
def pintura_parede():
    custo = 0
    lata = 0
    litro = 0
    area = int(input('informe o tamanho em metros quadrados da área que será pintada...\n'))
    litro = area / 3
    print(f' Você ira usar {litro} litros')
    lata = litro / 18
    print(f' Você irá utilizar {lata} latas')
    custo = lata * 80
    print(f' Seu custo será de {custo} reais')

# exerc 12
def resolv_equacao():
    a = float(input('Escreva o 1° coeficiente da equação...\n'))
    b = float(input('Escreva o 2° coeficiente da equação...\n'))
    c = float(input('Escreva o 3° coeficiente da equação...\n'))
    delta = b**2-4*a*c
    raiz_delta = delta**0.5
    raiz1 = (-b+raiz_delta)/(2*a)
    raiz2 = (-b-raiz_delta)/(2*a)
    print(f' as raizes serão {raiz1} e {raiz2}')

# exerc 18 ---> dúvida
def sequenc_fibona():
    sequencia = int(input('Quantos numeros você quer que seja demonstrado ?\n'))
    n1 = 0
    n2 = 1
    cont = 3
    while cont <= sequencia:
        n3 = n1 + n2
        cont = cont + 1

# exerc 21
def votação():
# candidato 1 = 20, candidato 2 = 50 candidato 3 = 60
    cont_1 = 0
    cont_2 = 0
    cont_3 = 0
    n = int(input('Quantos eleitores são ?\n'))
    for c in range(0,n):
        voto = int(input('Qual o seu voto ?\n'))
        if voto == 20:
            cont_1 = cont_1 + 1
        elif voto == 50:
            cont_2 = cont_2 + 1
        elif voto == 60:
            cont_3 = cont_3 + 1
    print(f' o candidado 1 teve {cont_1} votos, o candidato 2 teve {cont_2} votos e o candidato 3 teve {cont_3} votos')



def main():
    peso_peixe()
    pintura_parede()
    resolv_equacao()
    votação()


if __name__ == '__main__':
    main()

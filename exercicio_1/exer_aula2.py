#aula 2
#exerc 12
def media_dez_num():
    soma = 0
    for c in range(1, 11):
        numero = int(input(f'Escreva o {c}° numero...\n'))
        soma = soma + numero
        resultado = soma/10
    print(f'A soma aritmetica é {resultado}')

#exerc 14
def converter_temp():
    celsius = 0
    F = float(input('Insira uma temperatura em fahrenheits para ser convertida para celsius...\n'))
    celsius = 5 * (F-32)/9
    print(f'A temperatura em celsius é {celsius}')

#exerc 11
def peso_elef():
    for c in range(1, 51):
        peso_e_ident = float(input(f'Qual seria o peso do elefante com identificação {c} ?'))
        if c == 1:
            maior = peso_e_ident
        else:
            if peso_e_ident > maior:
                maior = peso_e_ident
    print(f' O elefante com maior peso é o {maior}')

def div_num():
    resto = 0
    num = float(input('escreva um número...\n'))
    resto = num % int(num)
    print(f'A parte fracionada é {resto}')
    print(f'A parte inteira é {int(num)}')

def main():
    media_dez_num()
    converter_temp()
    peso_elef()
    div_num()

if __name__=='__main__':
    main()
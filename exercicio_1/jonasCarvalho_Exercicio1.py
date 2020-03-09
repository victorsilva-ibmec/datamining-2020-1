#!/usr/bin/env python
# coding: utf-8


def exercicio_8(valor):
    parteInteira = int(valor)
    parteFracionada = valor - parteInteira 
    print('\nInteiro: ' + str(parteInteira) + '\nFracionado: ' +  str(parteFracionada))


'''Olha professor...  
Esse exercício é de cair o c* da bunda hein... Quero ver como isto poderia ser feito em Python básico
pois não vejo como poderíamos rastreiar o Id com o maior Peso sem utilizar uma matrix ou dicionário.
Bom... Demorei mas acho que consegui entregar uma solução elegante. '''
def exercicio_11():
    n_Boi = 50
    listaId = []
    listaPeso = []
    for n in range(n_Boi):
        identidade,peso = input("Digite a id e o peso separados por vírgula: ").split(',')
        
        listaId.append(identidade)
        listaPeso.append(float(peso))
        
    lista_Selecionado = list(max(zip(listaPeso,listaId)))
        
    print("\nBoi + Pesado \n\nID: " + str(lista_Selecionado[1] + "\nPeso: " + str(lista_Selecionado[0]) + "\n"))


def exercicio_12():
    n_Termos = 10
    soma = 0
    for n in range(n_Termos):
        num = int(input("Digite um numero (" + str(n) + "/" + str(n_Termos) + "): "))
        soma += num
    resultado = soma / n_Termos
    print('Média aritmética: ' + str(resultado))


def exercicio_14(valor_fah):
    valor_celsius = (5*(valor_fah - 32))/9
    print('\nCelsius: ' + str(valor_celsius))


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





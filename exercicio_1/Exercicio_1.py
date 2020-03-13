#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Template para os exercicios 8, 11, 12 e 14 da Aula 02."""
def exercicio_8(valor):
    
    inteiro = int(valor)
    fracionario = valor - inteiro
    
    print('parte inteira:', inteiro, 'parte fracionaria:',fracionario)
    


def exercicio_11():
    num_boi = 3
    
    peso_max = 0
    id_max = 0 
    
    for i in range (num_boi):
        id_boi = int(input('Digite o numero da identificação do boi:'))
        peso_boi = int(input('Digite o peso do boi: '))
        
        if peso_boi > peso_max:
            peso_max = peso_boi
            id_max = id_boi
    print('O boi mais pesado é o com o identificação:', id_max, 'com peso de:', peso_max)
    


def exercicio_12():
    soma = 0
    quant_num = 10
    for i in range(quant_num):
        num = float(input('Digiti um número: '))
        soma = soma + num 
        
    media = soma / quant_num 
    
    print('A média aritmética dos números é:', media)


def exercicio_14(valor_fah):
    celsius = (5*((valor_fah) - 32))/9
     
    print('A temperatura convertida para celsius é:', celsius)


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


# 

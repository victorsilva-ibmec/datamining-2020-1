#!/usr/bin/env python
# coding: utf-8

# In[ ]:


vetor1 = ['1', '3', '5', '7', '9', '11', '13', '15', '17', '19']
vetor2 = ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20']

def intercala_Lista(lista1,lista2):
    if len(lista1) != 10 or len(lista2) != 10:
        return "List size not applicable"
    else: 
        lista = list(zip(lista1,lista2))
        return [ocorrencia for sublista in lista for ocorrencia in sublista]

intercala_Lista(vetor1,vetor2)


# In[ ]:


def resumo_temp():
    listaMes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    listaTemp = []
    for mes in listaMes:
        tempInput = float(input(f"Digite a temperatura média de {mes}: "))
        listaTemp.append(tempInput)
    
    mediaAnual = sum(listaTemp)/len(listaTemp)
    
    for mes, temp in list(zip(listaMes,listaTemp)):
        if temp > mediaAnual:
            print(f'\n{mes} - {temp}')
    
    return None
        
resumo_temp()


# In[ ]:


def exercicio14():
    listaA = []
    while True:
        a = float(input('Digite a nota do aluno: '))
        if a != -1:
            listaA.append(a)
        else:
            break
    
    quantid = len(listaA)
    soma = sum(listaA)
    media = sum(listaA)/len(listaA)
    
    print(f'Quantidade de notas: {quantid}.')
    print(f'Notas ordenadas: {listaA}')
    print(f'Notas em ordem invertida: {listaA[::-1]}')
    print(f'Soma das notas: {soma}')
    print(f'Média das notas: {media}')
    print([n for n in listaA if n > media])
    
    return ("Programa efetuado e encerrado.")


exercicio14()


# In[ ]:





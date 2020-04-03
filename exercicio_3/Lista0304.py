

def ex10():
    lst1 = []
    lst2 = []
    lst3 = []
    for cont in range(10):
        valor1 = int(input('Informe um inteiro.'))
        valor2 = int(input('Informe um inteiro.'))
        lst1.append(valor1)
        lst2.append(valor2)
        lst3.append(valor1)
        lst3.append(valor2)
    print(lst3)



def ex12():
lst = []

  for cont in range(12):

   temp = float(input('Informe a temperatura do mes: '))
   lst.append(temp)

med = sum(lst) / len(lst)

i = 0
lstmaior = []
for temp in lst:
    i = i+1
 if temp > med:
    if  lst = 1
    mes = '1 - Janeiro'
  elif   lst = 2
    mes = '2 - Fevereiro'
  elif   lst = 3
    mes = '3 - Março'
  elif   lst = 4
    mes = '4 - Abril'
  elif   lst = 5
    mes = '5 - Maio'
elif   lst = 6
    mes = '6 - Junho'
  elif   lst = 7
    mes = '7 - Julho'
  elif   lst = 8
    mes = '8 - Agosto'
  elif   lst = 9
    mes = '9 - Setembro'
  elif   lst = 10
    mes = '10 - Outubro'
  elif   lst = 11
    mes = '11 - Novembro'
  elif   lst = 12
    mes = '12 - Dezembro'
  lstmaior.append(mes)

 print(lstmaior)



def ex14():
    lst = []
    cont = 1
      while True:
        Nota = float(input('Insira uma nota'))
        if nota <> -1:
         lst.append(nota)
         cont = cont + 1
        else:
            break
    print(len(lst))
    print(lst)
    print(lst[cont - (cont-1)])
    print(sum(lst))
    print(sum(lst)/len(lst))
    print('Volte Sempre!')






def main():
    ex10()


if __name__ == '__main__':
    main()
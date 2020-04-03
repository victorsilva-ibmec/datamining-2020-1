def procura_aluno(nome):
    '''Busca o índice na lista alunos que tenha o valor nome.'''
    if nome in alunos:
        print(f'O aluno procurado está na posição {alunos.index(nome)}.')
    else:
        print('Não existe ninguém com esse nome!')


def ex_10():
    lst1 = []
    lst2 = []
    lst3 = []
    for i in range(10):
        valor1 = int(input('Insira um valor para a primeira lista: '))
        lst1.append(valor1)
        valor2 = int(input('Insira um valor para a segunda lista: '))
        lst2.append(valor2)
    print(lst1)
    print(lst2)
    for i in range(10):
        lst3.append(lst1[i])
        lst3.append(lst2[i])
    print(lst3)


def ex_12():
    lst = []
    meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    for i in range(12):
        valor = int(input(f'Insira a temperatura nédia do mês {meses[i]}: '))
        lst.append(valor)
    med_anual = sum(lst) / 12
    print('A temperatura média anual foi: ',med_anual)
    for i, valor in enumerate(lst):
        if valor > med_anual:
            print(f'O mês de {meses[i]} teve a temperatura média de', valor, ', ficando acima da média anual.')
        else:
            pass


def ex_14():
    lst = []
    cont_notas = 0
    while True:
        num = float(input('Insira uma nota: '))
        if num == -1:
            break
        else:
            lst.append(num)
    print('Foram inseridas ', len(lst), 'notas.')
    print('As notas informadas foram:',lst)
    for i in range(len(lst)):
        print(len(lst) - i)
    print(f'A soma das notas é {sum(lst)}')
    print(f'A média das notas é {sum(lst) / len(lst)}')
    for num in lst:
        if num > (sum(lst) / len(lst)):
            cont_notas +=1
        else:
            pass
    print(f'Nota(s) acima da média: {cont_notas}.')
    print('\nPrograma finalizado.')



def main():
    ex_14()


if __name__ == '__main__':
    main()


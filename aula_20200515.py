from matplotlib import pyplot
from collections import Counter

def pib_linha():
  anos = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
  pib = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

  pyplot.plot(
    anos,
    pib,
    color='green',
    marker='o',
    linestyle='solid')
  pyplot.title('PIB nominal')
  pyplot.ylabel('Bilhoes de $')
  pyplot.show()

# List comprehension
def listcomp():
  nums = [1, 4, 5, 10, 20]
  nums2 = []
  for num in nums:
    nums2.append(num ** 2)

  nums2_alt = [x ** 2 for x in nums]
  print(nums2)
  print(nums2_alt)

def filmes_barras():
  filmes = ['Annie Hall', 'Ben-Hur', 'Casablanca',
            'Gandhi', 'West Side Story']
  num_oscars = [5, 11, 3, 8, 10]

  xs = [i for i in range(len(filmes))]
  pyplot.bar(xs, num_oscars)

  pyplot.ylabel('# de premiacoes')
  pyplot.title('Filmes e numero de Oscars')

  pyplot.xticks([i for i in range(len(filmes))], filmes)
  pyplot.show()

def tend_linhas():
  serie1 = [1, 2, 4, 8, 16, 32, 64, 128, 256]
  serie2 = [256, 128, 64, 32, 16, 8, 4, 2, 1]
  serie3 = [x + y for x, y in zip(serie1, serie2)]

  xs = [i for i in range(len(serie1))]

  pyplot.subplots(121)
  pyplot.plot(xs, serie1, 'g-', label='serie 1')
  pyplot.plot(xs, serie2, 'r-.', label='serie 2')
  pyplot.plot(xs, serie3, 'b:', label='serie 3')

  pyplot.legend(loc=9) # topo centro
  pyplot.xlabel('distribuicao de series')
  pyplot.title('Varias series')
  pyplot.show()

def tempo_amigos_disp():
  amigos = [70, 65, 72, 63, 71, 64, 60, 64, 67]
  minutos = [175, 170, 205, 120, 220, 130, 105, 145, 190]
  rotulos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

  pyplot.scatter(amigos, minutos)
  for rotulo, cont_amigo, cont_minuto in zip(rotulos, amigos, minutos):
    pyplot.annotate(
      rotulo,
      xy=(cont_amigo, cont_minuto),
      xytext=(5, -5),
      textcoords='offset points'
    )

  pyplot.title('Minutos diarios vs Numero de amigos')
  pyplot.xlabel('# de amigos')
  pyplot.ylabel('minutos diarios passados no site')
  pyplot.show()

def mediana(dados):
  n = len(dados)
  dados_ord = sorted(dados)
  ponto_medio = n // 2 # retorna um inteiro

  if n % 2 == 1:
    return dados_ord[ponto_medio]
  else:
    n1 = dados_ord[ponto_medio - 1]
    n2 = dados_ord[ponto_medio]
    return (n1 + n2) / 2

def quantil(dados, perc):
  if perc < 0 or perc > 1:
    return None

  p_indice = int(perc * len(dados))
  return sorted(dados)[p_indice]

def moda(dados):
  conts = Counter(dados) # {100: 1, 40: 4, 5: 4, ...}
  max_cont = max(conts.values())
  return [x for x in conts.keys() if conts[x] == max_cont]

def estatistica(dados):
  # numero de pontos nos dados
  num_pontos = len(dados)
  print(num_pontos)
  # maiores e menores valores
  maior_valor = max(dados)
  menor_valor = min(dados)
  print(maior_valor, menor_valor)
  # valores em posicoes especificas
  dados_ord = sorted(dados)
  segundo_menor_valor = dados_ord[1]
  segundo_maior_valor = dados_ord[-2]
  print(segundo_maior_valor, segundo_menor_valor)
  # valor medio, mediana, quantil, moda
  media = sum(dados) / len(dados)
  print(media)
  print(mediana(dados))
  print(quantil(dados, 0.01))
  print(quantil(dados, 0.75))
  print(moda(dados))

def amig_hist():
  num_amigos = [100, 49, 41, 40, 25, 50, 36, 28, 16, 40, 32, 32, 40, 49, 25, 40, 28, 18, 23, 5, 10, 5, 5, 5, 10]

  cont_amigos = Counter(num_amigos)
  xs = range(101)
  ys = [cont_amigos[x] for x in xs]

  pyplot.bar(xs, ys)
  pyplot.axis([0, 101, 0, 5])
  pyplot.title('Histograma de contagem de amigos')
  pyplot.xlabel('# de amigos')
  pyplot.ylabel('# de pessoas')
  pyplot.show()

  estatistica(num_amigos)

def amig_hist2():
  num_amigos = [100, 49, 41, 40, 25, 50, 36, 28, 16, 40, 32, 32, 40, 49, 25, 40, 28, 18, 23, 5, 10, 5, 5, 5, 10]

  pyplot.hist(num_amigos, bins=100)
  pyplot.show()

















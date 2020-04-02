def exer12():
    tempo = []
    for cont in range(12):
        temperatura = int(input("Qual a temperatura ? "))
        tempo.append(temperatura)

    Media = int (sum(tempo)/12)
    print(" Tempo:" + str(tempo), " - Media: " + str(Media))

    for i in range(12):
        if tempo[i] > Media:
            if i==0:
                print(str(i+1) + " - Janeiro, ")
            elif i==1:
                print(str(i+1) + " - Fevereiro, ")
            elif i == 2:
                print(str(i+1) + " - Marco, ")
            elif i == 3:
                print(str(i+1) + " - Abril, ")
            elif i == 4:
                print(str(i+1) + " - Maio, ")
            elif i == 5:
                print(str(i+1) + " - Junho, ")
            elif i == 6:
                print(str(i+1) + " - Julho, ")
            elif i == 7:
                print(str(i+1) + " - Agosto, ")
            elif i == 8:
                print(str(i+1) + " - Setembro, ")
            elif i == 9:
                print(str(i+1) + " - Outubro, ")
            elif i == 10:
                print(str(i+1) + " - Novembro, ")
            elif i == 11:
                print(str(i+1) + " - Dezembro, ")


def main():
    exer12()

main()
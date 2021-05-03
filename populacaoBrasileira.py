#Crescimento da Populacao Brasileira 1980-2019
#DataSus
import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()
x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x, y, color = "#e4e4e4")
plt.plot(x, y, color = "k", linestyle = "--")

plt.title("Crescimento da Populacao Brasileira 1980-2019")
plt.xlabel("Ano")
plt.ylabel("População x100.000")
plt.ticklabel_format(axis="y", style="sci", scilimits=(6,6))

#plt.show()
plt.savefig("Crescimento-da-Populacao-Brasileira-1980-2019.png", dpi = 500)
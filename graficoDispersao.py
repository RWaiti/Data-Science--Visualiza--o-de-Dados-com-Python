import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

title = "ScatterPlot: Gráfico de Dispersão"
XAxis = "Eixo X"
YAxis = "Eixo Y"

#Legendas
plt.title(title)
plt.xlabel(XAxis)
plt.ylabel(YAxis)

plt.scatter(x1, y1, label = "Meus Pontos", color = "r")
#liga os pontos do gráfico
plt.plot(x1,y1)

plt.legend()
plt.show()
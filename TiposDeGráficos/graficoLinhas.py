import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 9, 15]

title = "Gráfico de Linhas"
XAxis = "Eixo X"
YAxis = "Eixo Y"

#Legendas
plt.title(title)
plt.xlabel(XAxis)
plt.ylabel(YAxis)

plt.plot(x1, y1)

plt.show()

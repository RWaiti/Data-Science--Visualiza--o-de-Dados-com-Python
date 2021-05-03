import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]
z = [200, 3000 ,400, 330, 100]

title = "ScatterPlot: Gráfico de Dispersão"
XAxis = "Eixo X"
YAxis = "Eixo Y"

#Legendas
plt.title(title)
plt.xlabel(XAxis)
plt.ylabel(YAxis)

#liga os pontos do gráfico
plt.plot(x1,y1, color = "#000000", linestyle = "--")
#pontos do gráfico
plt.scatter(x1, y1, label = "Meus Pontos", color = "k", marker = ".", s= z)

plt.legend()
#Mostra o gráfico na Execução
#plt.show()
#Salva direito em figura - DPI = Pontos por Polegada, quanto maior o dpi maior a quantidade de pixels
plt.savefig("figura1.png", dpi = 500)
#Salva em formato pdf(vetor) - Pode alterar o zoom sem perder a resolução
plt.savefig("figura1.pdf")

'''
Documentação Oficial MatplotLib
Fonte: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
Markers

character	description
'.'	point marker
','	pixel marker
'o'	circle marker
'v'	triangle_down marker
'^'	triangle_up marker
'<'	triangle_left marker
'>'	triangle_right marker
'1'	tri_down marker
'2'	tri_up marker
'3'	tri_left marker
'4'	tri_right marker
'8'	octagon marker
's'	square marker
'p'	pentagon marker
'P'	plus (filled) marker
'*'	star marker
'h'	hexagon1 marker
'H'	hexagon2 marker
'+'	plus marker
'x'	x marker
'X'	x (filled) marker
'D'	diamond marker
'd'	thin_diamond marker
'|'	vline marker
'_'	hline marker
Line Styles

character	description
'-'	solid line style
'--'	dashed line style
'-.'	dash-dot line style
':'	dotted line style
Example format strings:

'b'    # blue markers with default shape
'or'   # red circles
'-g'   # green solid line
'--'   # dashed line with default color
'^k:'  # black triangle_up markers connected by a dotted line
Colors

The supported color abbreviations are the single letter codes

character	color
'b'	blue
'g'	green
'r'	red
'c'	cyan
'm'	magenta
'y'	yellow
'k'	black
'w'	white
'''